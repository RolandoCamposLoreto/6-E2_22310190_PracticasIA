# Q-Learning - Ejemplo básico

import numpy as np

# Parámetros del entorno
n_states = 5
n_actions = 2
gamma = 0.9  # Factor de descuento
alpha = 0.1  # Tasa de aprendizaje
epsilon = 0.1  # Tasa de exploración

# Inicialización de la tabla Q
Q = np.zeros((n_states, n_actions))

# Definir el entorno de recompensas
rewards = np.array([[0, 1], [1, 0], [0, 0], [0, 0], [0, 1]])

# Función para elegir la acción con epsilon-greedy
def epsilon_greedy(Q, state, epsilon):
    if np.random.rand() < epsilon:
        return np.random.choice(n_actions)  # Exploración
    else:
        return np.argmax(Q[state])  # Explotación

# Algoritmo Q-learning
def Q_learning(Q, rewards, gamma, alpha, epsilon, n_episodes=100):
    for _ in range(n_episodes):
        state = np.random.randint(0, n_states)  # Estado inicial aleatorio
        done = False
        while not done:
            action = epsilon_greedy(Q, state, epsilon)
            next_state = (state + 1) % n_states  # Transición aleatoria
            reward = rewards[state][action]
            Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
            state = next_state
            done = np.random.rand() < 0.1  # Probabilidad de finalización del episodio
    return Q

# Entrenar al agente
Q = Q_learning(Q, rewards, gamma, alpha, epsilon)
print("Tabla Q después de Q-learning:")
print(Q)
