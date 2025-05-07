import heapq

class NodoAStar:
    def __init__(self, estado, costo, heuristica, padre=None):
        self.estado = estado  # Almacenar el estado del nodo
        self.costo = costo  # El costo acumulado desde el nodo inicial hasta este nodo
        self.heuristica = heuristica  # La heurística (distancia estimada al objetivo)
        self.padre = padre  # El nodo padre, necesario para reconstruir el camino
        self.f = costo + heuristica  # La función f, que es la suma del costo y la heurística

    def __lt__(self, other):
        return self.f < other.f  # Comparar nodos por su función f (para usar en la estructura heapq)

def busqueda_A_estrella(estado_inicial, estado_objetivo, obtener_heuristica, obtener_vecinos):
    frontera = []  # Lista de nodos a explorar (usando un heap para obtener el nodo con el menor f)
    # Crear el nodo inicial y agregarlo a la frontera
    heapq.heappush(frontera, NodoAStar(estado_inicial, 0, obtener_heuristica(estado_inicial)))
    visitados = set()  # Conjunto para almacenar los estados ya visitados
    
    while frontera:  # Mientras haya nodos en la frontera
        nodo_actual = heapq.heappop(frontera)  # Obtener el nodo con el menor f de la frontera
        
        if nodo_actual.estado == estado_objetivo:  # Si hemos llegado al objetivo
            path = []
            while nodo_actual:  # Reconstruir el camino desde el objetivo hacia el inicio
                path.append(nodo_actual.estado)  # Agregar el estado al camino
                nodo_actual = nodo_actual.padre  # Subir al nodo padre
            return path[::-1]  # Retornar el camino invertido (del inicio al objetivo)
        
        visitados.add(nodo_actual.estado)  # Marcar el nodo actual como visitado
        
        for vecino in obtener_vecinos(nodo_actual.estado):  # Iterar sobre los vecinos del nodo actual
            if vecino not in visitados:  # Si el vecino no ha sido visitado
                costo = nodo_actual.costo + 1  # El costo es el costo del nodo actual + 1 (suponiendo costo uniforme)
                heuristica = obtener_heuristica(vecino)  # Calcular la heurística para el vecino
                nuevo_nodo = NodoAStar(vecino, costo, heuristica, nodo_actual)  # Crear un nuevo nodo para el vecino
                heapq.heappush(frontera, nuevo_nodo)  # Agregar el nuevo nodo a la frontera
                
    return None  # Si no se encuentra un camino, retornar None
