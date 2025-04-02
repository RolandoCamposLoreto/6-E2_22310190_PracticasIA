from grafos import Nodo

def crea_nodo_raiz(problema, estado=None):
    """Crea y devuelve el nodo raíz del problema indicado."""
    estado_raiz = estado or problema.estado_inicial
    acciones_raiz = {}
    if estado_raiz.nombre in problema.acciones.keys():
        acciones_raiz = problema.acciones[estado_raiz.nombre]
    raiz = Nodo(estado_raiz, acciones=acciones_raiz)
    raiz.coste = 0
    return raiz


def crea_nodo_hijo(problema, padre, accion):
    """Crea y devuelve el nodo hijo."""
    nuevo_estado = problema.resultado(padre.estado, accion)
    acciones_nuevo = {}
    if nuevo_estado.nombre in problema.acciones.keys():
        acciones_nuevo = problema.acciones[nuevo_estado.nombre]
    hijo = Nodo(nuevo_estado, accion, acciones_nuevo, padre)
    coste = padre.coste
    coste += problema.coste_accion(padre.estado, accion)
    hijo.coste = coste
    padre.hijos.append(hijo)
    return hijo