import numpy as np  # Importamos la librería NumPy para manejar arreglos y operaciones numéricas.

# Definir el entorno: un simple proceso de Markov con 3 estados
n_states = 3  # Número de estados en el proceso de Markov
n_actions = 2  # Número de acciones posibles por estado
rewards = np.array([[0, 1], [0, 0], [1, 0]])  # Recompensas para cada estado-acción (matriz 3x2).

# Función de valor estimada: inicializamos los valores para los 3 estados.
V = np.zeros(n_states)  # Inicialización de la función de valor para cada estado en 0.

# Política fija: el agente siempre elige la acción 0
policy = [0, 0, 0]  # Política fija donde el agente elige siempre la acción 0.

# Definir el modelo de transición de probabilidades entre estados
P = np.array([  # Matriz de probabilidades de transición para cada acción en cada estado.
    [[0.8, 0.2], [0.5, 0.5], [0.6, 0.4]],  # Estado 0: Probabilidades de transición para las acciones 0 y 1.
    [[0.6, 0.4], [0.4, 0.6], [0.7, 0.3]],  # Estado 1: Probabilidades de transición para las acciones 0 y 1.
    [[0.9, 0.1], [0.7, 0.3], [0.8, 0.2]],  # Estado 2: Probabilidades de transición para las acciones 0 y 1.
])

# Algoritmo de Evaluación de Política para RL Pasivo
def policy_evaluation(P, rewards, V, policy, gamma=0.9, tol=1e-6):
    delta = float('inf')  # Inicialización de delta como un valor infinito para la convergencia.
    while delta > tol:  # Mientras que la diferencia en los valores de los estados sea mayor que la tolerancia
        delta = 0  # Reiniciamos delta en cada iteración.
        for s in range(n_states):  # Iteramos sobre cada estado
            v = V[s]  # Guardamos el valor actual del estado s.
            # Actualizamos el valor del estado s según la política fija
            V[s] = sum(P[s][policy[s]] * (rewards[s][policy[s]] + gamma * V[s_prime]) for s_prime in range(n_states))
            delta = max(delta, abs(v - V[s]))  # Calculamos la diferencia máxima en la actualización de los valores.
    return V  # Devolvemos los valores actualizados de los estados.

# Evaluar la política con el modelo definido
V = policy_evaluation(P, rewards, V, policy)  # Llamamos a la función de evaluación de política.
print("Valor estimado de la política fija:", V)  # Mostramos los valores estimados para cada estado de acuerdo a la política.
