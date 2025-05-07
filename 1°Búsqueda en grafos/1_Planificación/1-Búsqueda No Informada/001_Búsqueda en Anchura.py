from grafos import Accion
from grafos import Estado
from grafos import Nodo
from grafos import Problema
from nodos import crea_nodo_raiz
from nodos import crea_nodo_hijo

def anchura(problema):
    """Búsqueda en grafos primero en anchura (breadth-first search)."""
    
    # Crear el nodo raíz, que es el nodo de inicio del problema
    raiz = crea_nodo_raiz(problema)
    
    # Si el nodo raíz es ya el objetivo, retornarlo inmediatamente
    if problema.es_objetivo(raiz.estado):
        return raiz
    
    # La frontera es una lista que contiene los nodos por explorar, empieza con el nodo raíz
    frontera = [raiz, ]
    
    # El conjunto explorados guarda los nodos que ya han sido procesados
    explorados = set()
    
    # Ciclo de búsqueda en anchura: continúa hasta que se encuentren todos los nodos o la frontera se quede vacía
    while True:
        # Si no hay más nodos en la frontera (es decir, ya no hay más nodos para explorar), termina la búsqueda
        if not frontera:
            return None
        
        # Se toma el primer nodo de la frontera
        nodo = frontera.pop(0)
        
        # Se marca el nodo actual como explorado
        explorados.add(nodo.estado)
        
        # Si el nodo no tiene acciones (es decir, no tiene nodos hijos), se continúa con el siguiente nodo de la frontera
        if not nodo.acciones:
            continue
        
        # Se recorre cada acción posible desde el nodo actual
        for nombre_accion in nodo.acciones.keys():
            # Se crea la acción y se genera el nodo hijo correspondiente a esa acción
            accion = Accion(nombre_accion)
            hijo = crea_nodo_hijo(problema, nodo, accion)
            
            # Se obtiene una lista con los estados de los nodos en la frontera para evitar ciclos
            estados_frontera = [nodo.estado for nodo in frontera]
            
            # Si el estado del hijo no ha sido explorado ni está en la frontera, lo procesamos
            if hijo.estado not in explorados and hijo.estado not in estados_frontera:
                # Se verifica si el hijo es el objetivo
                es_objetivo = problema.es_objetivo(hijo.estado)
                
                # Si el hijo es el objetivo, se retorna ese nodo
                if es_objetivo:
                    return hijo
                
                # Si no es el objetivo, se agrega el hijo a la frontera para seguir explorando
                frontera.append(hijo)
