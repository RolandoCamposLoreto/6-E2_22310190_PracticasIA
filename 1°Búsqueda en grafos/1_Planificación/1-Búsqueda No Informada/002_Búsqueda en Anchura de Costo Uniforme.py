from grafos import Accion
from grafos import Estado
from grafos import Nodo
from grafos import Problema
from nodos import crea_nodo_raiz
from nodos import crea_nodo_hijo

def coste_uniforme(problema):
    """Búsqueda en grafos de coste uniforme (uniform-cost search)."""
    
    # Crear el nodo raíz, que es el nodo de inicio del problema
    raiz = crea_nodo_raiz(problema)
    
    # La frontera contiene los nodos por explorar. Se inicia con el nodo raíz.
    frontera = [raiz, ]
    
    # El conjunto explorados guarda los nodos que ya han sido procesados
    explorados = set()
    
    # Ciclo de búsqueda: continúa hasta que se encuentren todos los nodos o la frontera se quede vacía
    while True:
        # Si no hay más nodos en la frontera (es decir, ya no hay más nodos para explorar), termina la búsqueda
        if not frontera:
            return None
        
        # Se toma el primer nodo de la frontera (con el coste más bajo debido al orden)
        nodo = frontera.pop(0)
        
        # Si el nodo es el objetivo, se retorna inmediatamente
        if problema.es_objetivo(nodo.estado):
            return nodo
        
        # Se marca el nodo actual como explorado
        explorados.add(nodo.estado)
        
        # Si el nodo no tiene acciones (es decir, no tiene nodos hijos), se continúa con el siguiente nodo
        if not nodo.acciones:
            continue
        
        # Se recorre cada acción posible desde el nodo actual
        for nombre_accion in nodo.acciones.keys():
            # Se crea la acción y se genera el nodo hijo correspondiente a esa acción
            accion = Accion(nombre_accion)
            hijo = crea_nodo_hijo(problema, nodo, accion)
            
            # Se obtiene una lista con los estados de los nodos en la frontera para evitar ciclos
            estados_frontera = [nodo.estado for nodo in frontera]
            
            # Si el hijo no ha sido explorado ni está en la frontera, lo agregamos a la frontera
            if hijo.estado not in explorados and hijo.estado not in estados_frontera:
                frontera.append(hijo)
            else:
                # Si el hijo ya está en la frontera, se compara su coste
                buscar = [nodo for nodo in frontera if nodo.estado == hijo.estado]
                
                # Si el hijo está en la frontera y tiene un menor coste que el nodo existente en la frontera,
                # lo reemplazamos por el hijo con el coste menor
                if buscar:
                    if hijo.coste < buscar[0].coste:
                        indice = frontera.index(buscar[0])
                        frontera[indice] = hijo
        
        # Ordenamos la frontera de menor a mayor coste para seguir explorando el nodo con el coste más bajo
        frontera.sort(key=lambda nodo: nodo.coste)
