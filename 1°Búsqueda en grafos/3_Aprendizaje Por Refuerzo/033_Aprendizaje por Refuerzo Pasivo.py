# Aprendizaje por Refuerzo Pasivo - Ejemplo básico

import numpy as np

# Definir el entorno: un simple proceso de Markov con 3 estados
n_states = 3
n_actions = 2
rewards = np.array([[0, 1], [0, 0], [1, 0]])  # Recompensas para cada estado-acción

# Función de valor estimada
V = np.zeros(n_states)

# Política fija
policy = [0, 0, 0]  # Establecemos que el agente siempre elige la acción 0

# Definir el modelo de transición de probabilidades
P = np.array([
    [[0.8, 0.2], [0.5, 0.5], [0.6, 0.4]],  # Estado 0
    [[0.6, 0.4], [0.4, 0.6], [0.7, 0.3]],  # Estado 1
    [[0.9, 0.1], [0.7, 0.3], [0.8, 0.2]],  # Estado 2
])

# Algoritmo de Evaluación de Política para RL Pasivo
def policy_evaluation(P, rewards, V, policy, gamma=0.9, tol=1e-6):
    delta = float('inf')
    while delta > tol:
        delta = 0
        for s in range(n_states):
            v = V[s]
            V[s] = sum(P[s][policy[s]] * (rewards[s][policy[s]] + gamma * V[s_prime]) for s_prime in range(n_states))
            delta = max(delta, abs(v - V[s]))
    return V

# Evaluar la política
V = policy_evaluation(P, rewards, V, policy)
print("Valor estimado de la política fija:", V)
