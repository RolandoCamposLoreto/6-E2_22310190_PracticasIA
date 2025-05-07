# Búsqueda de la Política - Ejemplo básico

import numpy as np

# Parámetros
n_states = 5
n_actions = 2
gamma = 0.9

# Inicialización de la tabla de valores V
V = np.zeros(n_states)

# Recompensas del entorno
rewards = np.array([[0, 1], [1, 0], [0, 0], [0, 0], [0, 1]])

# Transiciones del entorno
P = np.array([
    [0.8, 0.2], [0.6, 0.4], [0.9, 0.1], [0.7, 0.3], [0.8, 0.2]
])

# Algoritmo de búsqueda de la política
def policy_search(V, rewards, P, gamma=0.9):
    policy = np.zeros(n_states)
    for s in range(n_states):
        action_values = []
        for a in range(n_actions):
            action_values.append(np.sum(P[s] * (rewards[s] + gamma * V)))
        policy[s] = np.argmax(action_values)
    return policy

# Encontrar la política óptima
optimal_policy = policy_search(V, rewards, P, gamma)
print("Política encontrada:")
print(optimal_policy)
