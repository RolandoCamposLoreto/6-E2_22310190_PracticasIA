import numpy as np  # Importamos numpy para realizar cálculos matemáticos y gestionar arreglos.

# Parámetros
n_states = 5  # Número de estados en el entorno.
n_actions = 2  # Número de acciones posibles en cada estado.
gamma = 0.9  # Factor de descuento para la evaluación de recompensas futuras.

# Inicialización de la tabla de valores V
V = np.zeros(n_states)  # Inicializamos la tabla de valores V con ceros. Cada valor de V[s] representa el valor del estado s.

# Recompensas del entorno
rewards = np.array([[0, 1], [1, 0], [0, 0], [0, 0], [0, 1]])  # Matriz de recompensas: para cada estado y acción, se asigna una recompensa.

# Transiciones del entorno (probabilidades de transición)
P = np.array([  # Probabilidades de transición para cada acción en cada estado.
    [0.8, 0.2],  # Probabilidades de transición para el estado 0.
    [0.6, 0.4],  # Probabilidades de transición para el estado 1.
    [0.9, 0.1],  # Probabilidades de transición para el estado 2.
    [0.7, 0.3],  # Probabilidades de transición para el estado 3.
    [0.8, 0.2],  # Probabilidades de transición para el estado 4.
])

# Algoritmo de búsqueda de la política
def policy_search(V, rewards, P, gamma=0.9):
    """
    Esta función implementa un algoritmo de búsqueda de política que busca la política óptima 
    dada una tabla de valores V, recompensas y probabilidades de transición.
    """
    policy = np.zeros(n_states)  # Inicializa la política con ceros (política inicial).
    
    # Recorremos cada estado para determinar la acción óptima.
    for s in range(n_states):
        action_values = []  # Lista que almacenará el valor de cada acción en el estado s.
        
        # Recorremos todas las posibles acciones para calcular el valor de cada una.
        for a in range(n_actions):
            # Calculamos el valor de la acción a en el estado s usando la fórmula de Bellman.
            action_values.append(np.sum(P[s] * (rewards[s] + gamma * V)))  # Se multiplica la probabilidad de transición por la recompensa y el valor futuro.
        
        # Asignamos la acción con el mayor valor esperado al estado s en la política.
        policy[s] = np.argmax(action_values)
    
    return policy  # Devolvemos la política óptima.

# Encontrar la política óptima utilizando el algoritmo de búsqueda de política.
optimal_policy = policy_search(V, rewards, P, gamma)
print("Política encontrada:")  # Imprimimos la política resultante.
print(optimal_policy)  # Mostramos la política óptima encontrada.
