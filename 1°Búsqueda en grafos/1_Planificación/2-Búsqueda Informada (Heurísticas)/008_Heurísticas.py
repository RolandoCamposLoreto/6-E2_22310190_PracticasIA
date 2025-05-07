from grafos import Accion
from grafos import Estado
from grafos import Nodo
from grafos import Problema
from nodos import crea_nodo_raiz
from nodos import crea_nodo_hijo
from frontera import sacar_siguiente

def voraz(problema):
    """Búsqueda en grafos voraz (greedy search)."""
    raiz = crea_nodo_raiz(problema)  # Crear el nodo raíz a partir del problema.
    frontera = [raiz, ]  # Inicializar la frontera con el nodo raíz.
    explorados = set()  # Conjunto para almacenar los estados explorados.
    while True:
        if not frontera:  # Si la frontera está vacía, no hay solución.
            return None
        nodo = sacar_siguiente(frontera, 'heuristica', objetivos=problema.estados_objetivos)  # Sacar el siguiente nodo basado en la heurística.
        if problema.es_objetivo(nodo.estado):  # Si el nodo es objetivo, se retorna.
            return nodo
        explorados.add(nodo.estado)  # Marcar el nodo como explorado.
        if not nodo.acciones:  # Si no hay acciones disponibles en el nodo, continuar con el siguiente ciclo.
            continue
        for nombre_accion in nodo.acciones.keys():  # Recorrer las acciones disponibles en el nodo.
            accion = Accion(nombre_accion)  # Crear la acción.
            hijo = crea_nodo_hijo(problema, nodo, accion)  # Crear un nodo hijo a partir de la acción.
            estados_frontera = [nodo.estado for nodo in frontera]  # Obtener los estados de los nodos en la frontera.
            if hijo.estado in explorados or hijo.estado in estados_frontera:  # Si el estado del hijo ya fue explorado o está en la frontera.
                buscar = [nodo for nodo in frontera if nodo.estado == hijo.estado]  # Buscar el nodo hijo en la frontera.
                if buscar:  # Si se encuentra el nodo hijo en la frontera.
                    heuristic_hijo = [hijo.heuristicas[objetivo.nombre] for objetivo in problema.estados_objetivos]  # Obtener las heurísticas del hijo.
                    heuristic_buscar = [buscar[0].heuristicas[objetivo.nombre] for objetivo in problema.estados_objetivos]  # Obtener las heurísticas del nodo en la frontera.
                    minimo_hijo = min(heuristic_hijo)  # Obtener el valor mínimo de la heurística del hijo.
                    minimo_buscar = min(heuristic_buscar)  # Obtener el valor mínimo de la heurística del nodo en la frontera.
                    if minimo_hijo < minimo_buscar:  # Si la heurística del hijo es mejor que la del nodo en la frontera.
                        indice = frontera.index(buscar[0])  # Obtener el índice del nodo en la frontera.
                        frontera[indice] = hijo  # Sustituir el nodo en la frontera por el hijo.
            else:  # Si el estado del hijo no está ni en los estados explorados ni en la frontera.
                frontera.append(hijo)  # Agregar el hijo a la frontera.
