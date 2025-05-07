from grafos import Accion
from grafos import Estado
from grafos import Nodo
from grafos import Problema
from nodos import crea_nodo_raiz
from nodos import crea_nodo_hijo

def bidireccional(problema):
    """Búsqueda que comienza en los nodos inicial y final a la vez."""
    # Crea el nodo raíz para el problema, partiendo tanto del estado inicial como del objetivo.
    raiz_i = crea_nodo_raiz(problema, problema.estado_inicial)
    raiz_f = crea_nodo_raiz(problema, problema.estados_objetivos[0])
    
    # Si el estado inicial ya es el objetivo, retorna el nodo inicial y el final.
    if problema.es_objetivo(raiz_i.estado):
        return (raiz_i, raiz_f)
    
    # Si el estado inicial y el final son el mismo, también se retorna.
    if problema.estado_inicial == raiz_f.estado:
        return (raiz_i, raiz_f)
    
    # Inicializa las fronteras de la búsqueda para los dos sentidos.
    frontera_i = [raiz_i, ]  # Frontera de la búsqueda desde el estado inicial.
    frontera_f = [raiz_f, ]  # Frontera de la búsqueda desde el estado objetivo.
    
    # Inicializa las listas de explorados para ambos sentidos.
    explorados_i = []  # Explorado desde el estado inicial.
    explorados_f = []  # Explorado desde el estado objetivo.

    while True:
        # Si alguna frontera se queda vacía, significa que no hay solución.
        if not frontera_i or not frontera_f:
            return (None, None)

        # Extrae un nodo de cada frontera para continuar la búsqueda.
        nodo_i = frontera_i.pop(0)
        nodo_f = frontera_f.pop(0)

        # Marca los nodos actuales como explorados en sus respectivos lados.
        explorados_i.append(nodo_i)
        explorados_f.append(nodo_f)

        # Expande el nodo actual de la frontera de inicio (estado inicial).
        resultado_i = amplia_frontera(problema, nodo_i, problema.estados_objetivos[0], frontera_i, explorados_i)
        if resultado_i:
            return (resultado_i, None)  # Si encuentra un nodo objetivo desde el inicio, retorna el resultado.

        # Expande el nodo actual de la frontera de fin (estado objetivo).
        resultado_f = amplia_frontera(problema, nodo_f, problema.estado_inicial, frontera_f, explorados_f)
        if resultado_f:
            return (None, resultado_f)  # Si encuentra un nodo objetivo desde el final, retorna el resultado.

        # Obtiene los estados explorados en ambas fronteras y sus uniones.
        estados_i = set(nodo.estado for nodo in frontera_i)
        estados_f = set(nodo.estado for nodo in frontera_f)
        estados_i = estados_i.union(set(nodo.estado for nodo in explorados_i))
        estados_f = estados_f.union(set(nodo.estado for nodo in explorados_f))

        # Busca la intersección entre los estados de ambas fronteras.
        comunes = estados_i.intersection(estados_f)
        if comunes:
            # Si hay un estado común, se detiene la búsqueda y se retorna ese estado.
            comun = comunes.pop()
            
            # Recolecta todos los nodos de las dos fronteras y los explorados.
            nodos_arbol_i = []
            nodos_arbol_f = []
            nodos_arbol_i.extend(frontera_i)
            nodos_arbol_f.extend(frontera_f)
            nodos_arbol_i.extend(explorados_i)
            nodos_arbol_f.extend(explorados_f)

            # Encuentra el nodo común en ambas listas.
            comun_i = [nodo for nodo in nodos_arbol_i if nodo.estado == comun][0]
            comun_f = [nodo for nodo in nodos_arbol_f if nodo.estado == comun][0]
            
            return (comun_i, comun_f)  # Retorna los nodos encontrados en las dos fronteras.

# Mueve la definición de 'amplia_frontera' fuera del bucle 'while True'
def amplia_frontera(problema, nodo, objetivo, frontera, explorados):
    # Expande el nodo actual generando todos sus hijos a partir de las acciones posibles.
    for nombre_accion in nodo.acciones.keys():
        accion = Accion(nombre_accion)
        hijo = crea_nodo_hijo(problema, nodo, accion)
        
        # Comprueba si el hijo ya está en las fronteras o en los explorados.
        estados_frontera = [nodo.estado for nodo in frontera]
        estados_explorados = [nodo.estado for nodo in explorados]
        
        # Si el hijo no ha sido explorado ni está en la frontera, lo añade a la frontera.
        if hijo.estado not in estados_explorados and hijo.estado not in estados_frontera:
            if objetivo == hijo.estado:  # Si el hijo es el objetivo, lo retorna.
                return hijo
            frontera.append(hijo)  # De lo contrario, lo añade a la frontera para seguir explorando.
    
    return None  # Si no encuentra ningún hijo objetivo, retorna None.
