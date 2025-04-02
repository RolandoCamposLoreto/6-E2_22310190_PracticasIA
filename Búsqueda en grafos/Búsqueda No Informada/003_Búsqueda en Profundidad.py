from grafos import Accion
from grafos import Estado
from grafos import Nodo
from grafos import Problema
from nodos import crea_nodo_raiz
from nodos import crea_nodo_hijo

def profundidad(problema):
    """Búsqueda en grafos primero en profundidad (depth-first search)."""
    
    # Crear el nodo raíz, que es el nodo de inicio del problema
    raiz = crea_nodo_raiz(problema)
    
    # Si el nodo raíz es el objetivo, lo retornamos inmediatamente
    if problema.es_objetivo(raiz.estado):
        return raiz
    
    # La frontera es una lista que contiene los nodos por explorar, comienza con el nodo raíz
    frontera = [raiz, ]
    
    # El conjunto explorados guarda los nodos que ya han sido procesados
    explorados = set()
    
    # Ciclo de búsqueda en profundidad: sigue hasta que no queden nodos en la frontera
    while True:
        # Si no hay más nodos en la frontera (es decir, ya no hay más nodos para explorar), termina la búsqueda
        if not frontera:
            return None
        
        # Se toma el último nodo de la frontera (por eso es una búsqueda en profundidad, usa un LIFO)
        nodo = frontera.pop()
        
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
                # Si el hijo es el objetivo, se retorna inmediatamente
                es_objetivo = problema.es_objetivo(hijo.estado)
                if es_objetivo:
                    return hijo
                
                # Si no es el objetivo, se agrega el hijo a la frontera para seguir explorando
                frontera.append(hijo)
