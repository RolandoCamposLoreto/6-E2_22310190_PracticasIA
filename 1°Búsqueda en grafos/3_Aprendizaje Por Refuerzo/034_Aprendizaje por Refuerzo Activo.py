import numpy as np  # Importamos la librería NumPy para trabajar con matrices y operaciones numéricas.

# Parámetros del entorno
n_states = 5  # Número de estados en el entorno
n_actions = 2  # Número de acciones posibles por estado
gamma = 0.9  # Factor de descuento para las recompensas futuras
alpha = 0.1  # Tasa de aprendizaje, determina cuán rápido el agente aprende
epsilon = 0.1  # Probabilidad de explorar (política epsilon-greedy)

# Inicialización de la tabla Q (tamaño n_states x n_actions, todos los valores inicializados a 0)
Q = np.zeros((n_states, n_actions))  # Tabla Q que almacena los valores Q para cada estado-acción.

# Definir el entorno de recompensas (una matriz simple de recompensas)
rewards = np.array([[0, 1], [1, 0], [0, 0], [0, 0], [0, 1]])  # Recompensas para cada estado-acción.

# Función para elegir la acción con política epsilon-greedy
def epsilon_greedy(Q, state, epsilon):
    # Si un número aleatorio es menor que epsilon, se elige una acción aleatoria (exploración).
    if np.random.rand() < epsilon:
        return np.random.choice(n_actions)  # Exploración: selecciona una acción aleatoria.
    else:
        return np.argmax(Q[state])  # Explotación: selecciona la acción con el mayor valor Q.

# Algoritmo de Aprendizaje por Refuerzo Activo (Q-learning)
def Q_learning(Q, rewards, gamma, alpha, epsilon, n_episodes=100):
    # El agente realiza aprendizaje a través de múltiples episodios.
    for _ in range(n_episodes):
        state = np.random.randint(0, n_states)  # Elige un estado inicial aleatorio.
        done = False  # Variable que indica si el episodio ha terminado.
        
        while not done:
            # Elige una acción basada en la política epsilon-greedy.
            action = epsilon_greedy(Q, state, epsilon)
            # Para este ejemplo, se realiza una transición aleatoria al siguiente estado.
            next_state = (state + 1) % n_states  # Transición cíclica (siguiente estado).
            reward = rewards[state][action]  # Recompensa obtenida por la acción realizada.

            # Actualización de la tabla Q usando la fórmula de Q-learning.
            Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
            
            # El agente se mueve al siguiente estado.
            state = next_state
            
            # Probabilidad de finalizar el episodio.
            done = np.random.rand() < 0.1  # 10% de probabilidad de finalizar el episodio.
    
    return Q  # Devolver la tabla Q aprendida al final de todos los episodios.

# Entrenar al agente mediante Q-learning.
Q = Q_learning(Q, rewards, gamma, alpha, epsilon)

# Mostrar la tabla Q aprendida después de entrenar al agente.
print("Tabla Q aprendida:")
print(Q)  # Imprimimos la tabla Q final después de los episodios de entrenamiento.
