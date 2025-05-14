import numpy as np  # Importamos la librería NumPy para manejar arreglos y realizar operaciones matemáticas.

# Parámetros del entorno
n_states = 5  # Número de estados en el entorno.
n_actions = 2  # Número de acciones posibles en cada estado.
gamma = 0.9  # Factor de descuento para las recompensas futuras.
alpha = 0.1  # Tasa de aprendizaje que determina qué tan rápido el agente ajusta su tabla Q.
epsilon = 0.1  # Probabilidad de explorar una acción aleatoria (política epsilon-greedy).

# Inicialización de la tabla Q con ceros.
# La tabla Q tiene un tamaño de (n_states x n_actions), ya que para cada estado tenemos una lista de acciones.
Q = np.zeros((n_states, n_actions))  # Inicializamos la tabla Q en cero.

# Definir el entorno de recompensas (un ejemplo simple de recompensas en función del estado y la acción).
rewards = np.array([[0, 1], [1, 0], [0, 0], [0, 0], [0, 1]])  # Recompensas para cada par estado-acción.

# Función para elegir la acción a tomar usando la política epsilon-greedy.
# La función elige aleatoriamente entre exploración (acción aleatoria) o explotación (acción que maximiza Q).
def epsilon_greedy(Q, state, epsilon):
    if np.random.rand() < epsilon:
        return np.random.choice(n_actions)  # Exploración: elegimos una acción aleatoria.
    else:
        return np.argmax(Q[state])  # Explotación: elegimos la acción con el valor Q más alto.

# Algoritmo de Q-learning para actualizar la tabla Q en función de la experiencia del agente.
def Q_learning(Q, rewards, gamma, alpha, epsilon, n_episodes=100):
    # El agente aprenderá durante un número de episodios.
    for _ in range(n_episodes):
        state = np.random.randint(0, n_states)  # Elige un estado inicial aleatorio.
        done = False  # Indicador de si el episodio ha terminado.
        
        while not done:
            # Elegimos una acción usando la política epsilon-greedy.
            action = epsilon_greedy(Q, state, epsilon)
            # Para este ejemplo, la transición al siguiente estado es cíclica (estado + 1).
            next_state = (state + 1) % n_states  # Transición cíclica entre los estados.
            reward = rewards[state][action]  # Recompensa obtenida por la acción elegida.

            # Actualización de la tabla Q usando la fórmula de Q-learning.
            # Actualizamos el valor Q de la acción tomada en el estado actual, según la recompensa y el valor del siguiente estado.
            Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
            
            # El agente se mueve al siguiente estado.
            state = next_state
            # Probabilidad de finalizar el episodio (10% de probabilidad de terminar).
            done = np.random.rand() < 0.1  # Un 10% de probabilidad de terminar el episodio en cada paso.
    
    return Q  # Devolvemos la tabla Q aprendida después de completar todos los episodios.

# Entrenar al agente usando el algoritmo de Q-learning.
Q = Q_learning(Q, rewards, gamma, alpha, epsilon)

# Imprimir la tabla Q final después de haber aprendido durante todos los episodios.
print("Tabla Q después de Q-learning:")
print(Q)  # Mostramos la tabla Q final aprendida.
