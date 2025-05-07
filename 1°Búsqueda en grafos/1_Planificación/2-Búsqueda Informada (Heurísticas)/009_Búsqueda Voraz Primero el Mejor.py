import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # Almacenar la posición del nodo
        self.parent = parent  # Almacenar el nodo padre (para reconstruir el camino)
        self.g = 0  # Costo desde el inicio (no se usa en búsqueda voraz, pero se incluye para compatibilidad con A*)
        self.h = 0  # Heurística (distancia estimada al objetivo)

    def __eq__(self, other):
        return self.position == other.position  # Comparar nodos por su posición

    def __lt__(self, other):
        return self.h < other.h  # Comparar nodos según la heurística (para usar en la estructura heapq)

def heuristic(a, b):
    # Función heurística: Calcula la distancia Manhattan entre dos puntos
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_best_first_search(start, goal, grid):
    open_list = []  # Lista de nodos a explorar
    closed_list = set()  # Conjunto de nodos ya explorados
    start_node = Node(start)  # Crear el nodo de inicio
    start_node.h = heuristic(start, goal)  # Calcular la heurística del nodo de inicio
    heapq.heappush(open_list, start_node)  # Agregar el nodo de inicio a la lista abierta

    while open_list:
        current_node = heapq.heappop(open_list)  # Obtener el nodo con la menor heurística de la lista abierta

        if current_node.position == goal:  # Si hemos llegado al objetivo, reconstruir el camino
            path = []
            while current_node:
                path.append(current_node.position)  # Agregar la posición del nodo al camino
                current_node = current_node.parent  # Subir al nodo padre
            return path[::-1]  # Retornar el camino invertido (del inicio al objetivo)

        closed_list.add(current_node.position)  # Marcar el nodo actual como explorado

        for neighbor in get_neighbors(current_node.position):  # Iterar sobre los vecinos del nodo actual
            # Si el vecino ya ha sido explorado o es un obstáculo (lago o cocodrilo), omitirlo
            if neighbor in closed_list or grid[neighbor[1]][neighbor[0]] == 1:
                continue

            # Crear el nodo vecino
            neighbor_node = Node(neighbor, current_node)
            neighbor_node.h = heuristic(neighbor, goal)  # Calcular la heurística del vecino
            if neighbor_node not in open_list:  # Si el vecino no está en la lista abierta, agregarlo
                heapq.heappush(open_list, neighbor_node)

    return None  # Si no se encuentra un camino, retornar None

def get_neighbors(position):
    # Función para obtener los vecinos ortogonales de una posición (arriba, abajo, izquierda, derecha)
    x, y = position
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

# Ejemplo de uso con una cuadrícula que contiene obstáculos
grid = [[0, 0, 0, 1, 0],  # 0: libre, 1: lago o cocodrilo
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]]

start = (0, 0)  # Posición de inicio
goal = (4, 4)  # Posición de destino
path = greedy_best_first_search(start, goal, grid)  # Llamada a la función de búsqueda

print("Ruta encontrada:", path)  # Imprimir la ruta encontrada
