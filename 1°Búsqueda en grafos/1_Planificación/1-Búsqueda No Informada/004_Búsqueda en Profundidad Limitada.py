from grafos import Accion
from grafos import Estado
from grafos import Nodo
from grafos import Problema

def dfs_profundidad_limitada(nodo, grafo, visitados, limite):
    # Si el límite de profundidad se alcanza (es decir, límite < 0), se termina la búsqueda.
    if limite < 0:
        return  # No exploramos más allá del límite de profundidad
    
    # Se marca el nodo como visitado
    visitados.add(nodo)
    
    # Se imprime el nodo visitado y la cantidad de profundidad restante
    print(f"Visitando: {nodo}, Límite restante: {limite}")
    
    # Se recorre cada vecino del nodo actual en el grafo
    for vecino in grafo.get(nodo, []):
        # Si el vecino no ha sido visitado, se hace una llamada recursiva
        if vecino not in visitados:
            # Llamada recursiva con un límite de profundidad reducido en 1
            dfs_profundidad_limitada(vecino, grafo, visitados, limite - 1)

# Ejemplo de uso del algoritmo:
grafo = {
    'A': ['B', 'C'],  # Nodo A tiene como vecinos a B y C
    'B': ['D', 'E'],  # Nodo B tiene como vecinos a D y E
    'C': ['F', 'G'],  # Nodo C tiene como vecinos a F y G
    'D': [],  # Nodo D no tiene vecinos
    'E': ['H'],  # Nodo E tiene como vecino a H
    'F': [],  # Nodo F no tiene vecinos
    'G': [],  # Nodo G no tiene vecinos
    'H': []  # Nodo H no tiene vecinos
}

# Se inicializa un conjunto de nodos visitados y un límite de profundidad de 2
visitados = set()
limite = 2  # Límite de profundidad máxima

# Se llama al algoritmo de búsqueda con el nodo inicial 'A'
dfs_profundidad_limitada('A', grafo, visitados, limite)
