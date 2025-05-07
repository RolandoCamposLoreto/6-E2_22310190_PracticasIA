from grafos import Accion
from grafos import Estado
from grafos import Nodo
from grafos import Problema
from nodos import crea_nodo_hijo

def profundidad_iterativa(problema, limite):
    """Versión iterativa de la búsqueda en profundidad."""
    # Si no se especifica un límite, se llama a la búsqueda en profundidad recursiva sin límite.
    if limite is None:
        return profundidad_recursiva(problema)
    
    # Si se da un límite, se realiza búsqueda con profundidades crecientes (iterativa).
    for i in range(1, limite + 1):
        # Para cada nivel de profundidad desde 1 hasta el límite, realiza la búsqueda recursiva
        resultado = profundidad_recursiva(problema, i)
        if resultado:
            return resultado  # Si se encuentra un resultado, se retorna.
    
    return None  # Si no se encuentra ningún resultado en ninguna profundidad, retorna None.

def profundidad_recursiva(problema, limite=99999):
    """Versión recursiva de la búsqueda en grafos primero en profundidad."""
    # Crea el nodo raíz del problema.
    raiz = crea_nodo_raiz(problema)
    explorados = set()  # Conjunto de nodos explorados para evitar ciclos.
    
    # Llama a la función recursiva que realiza la búsqueda en profundidad.
    return __bpp_recursiva(raiz, problema, limite, explorados)

def crea_nodo_raiz(problema, estado=None):
    """Crea y devuelve el nodo raíz del problema indicado."""
    # Si no se pasa un estado específico, utiliza el estado inicial del problema.
    estado_raiz = estado or problema.estado_inicial
    
    # Inicializa el diccionario de acciones para el nodo raíz.
    acciones_raiz = {}
    if estado_raiz.nombre in problema.acciones.keys():
        acciones_raiz = problema.acciones[estado_raiz.nombre]
    
    # Crea el nodo raíz con el estado y las acciones asociadas.
    raiz = Nodo(estado_raiz, acciones=acciones_raiz)
    raiz.coste = 0  # El coste del nodo raíz es 0.
    return raiz

def __bpp_recursiva(nodo, problema, limite, explorados):
    """Función recursiva para realizar la búsqueda primero en profundidad."""
    # Si el nodo actual es el objetivo, devuelve el nodo.
    if problema.es_objetivo(nodo.estado):
        return nodo
    
    # Si se alcanza el límite de profundidad, retorna None para no explorar más allá.
    if limite == 0:
        return None
    
    # Marca el nodo actual como explorado.
    explorados.add(nodo.estado)
    
    # Si el nodo no tiene acciones, no puede generar nodos hijos, por lo que retornamos None.
    if not nodo.acciones:
        return None
    
    # Recorre todas las acciones posibles del nodo actual.
    for nombre_accion in nodo.acciones.keys():
        accion = Accion(nombre_accion)
        hijo = crea_nodo_hijo(problema, nodo, accion)  # Crea el hijo correspondiente al realizar la acción.
        
        # Si el hijo no ha sido explorado, lo explora recursivamente.
        if hijo.estado not in explorados:
            # Realiza una llamada recursiva a la función para el hijo con límite reducido.
            resultado = __bpp_recursiva(hijo, problema, limite - 1, explorados.copy())
            if resultado:
                return resultado  # Si se encuentra un resultado, se retorna.
    
    return None  # Si no se encuentra ningún resultado, retorna None.
