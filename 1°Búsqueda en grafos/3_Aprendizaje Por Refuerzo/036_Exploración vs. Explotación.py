# Exploración vs. Explotación - Ejemplo básico con una política epsilon-greedy

import numpy as np

# Inicialización de las tablas de valor Q
n_states = 5
n_actions = 2
Q = np.zeros((n_states, n_actions))

# Parámetros
gamma = 0.9
epsilon = 0.1  # Control de exploración

# Función epsilon-greedy
def epsilon_greedy(Q, state, epsilon):
    if np.random.rand() < epsilon:
        return np.random.choice(n_actions)  # Exploración
    else:
        return np.argmax(Q[state])  # Explotación

# Simulación simple de exploración vs. explotación
def exploration_vs_exploitation(Q, epsilon, n_episodes=100):
    for _ in range(n_episodes):
        state = np.random.randint(0, n_states)
        action = epsilon_greedy(Q, state, epsilon)
        print(f"Estrategia de acción en estado {state}: {'Exploración' if action != np.argmax(Q[state]) else 'Explotación'}")
        
exploration_vs_exploitation(Q, epsilon)
