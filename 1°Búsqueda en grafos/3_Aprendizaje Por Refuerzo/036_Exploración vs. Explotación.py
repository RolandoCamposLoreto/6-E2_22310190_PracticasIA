import numpy as np  # Importamos la librería numpy, que proporciona funciones para trabajar con matrices y realizar cálculos matemáticos.

# Inicialización de las tablas de valor Q
n_states = 5  # Definimos que hay 5 estados posibles en el entorno.
n_actions = 2  # Definimos que hay 2 acciones posibles para cada estado.

# Inicializamos la tabla Q con ceros. La tabla Q tiene un tamaño de (n_states, n_actions), 
# es decir, 5 estados por 2 acciones. Cada valor de Q[i, j] representa el valor de la acción j en el estado i.
Q = np.zeros((n_states, n_actions))  # Inicializamos Q con ceros, lo que significa que no tenemos información sobre el valor de las acciones.

# Parámetros de la simulación
gamma = 0.9  # Factor de descuento que se usa para la actualización de los valores en Q-learning. Controla la importancia de las recompensas futuras.
epsilon = 0.1  # Control de exploración. Con probabilidad epsilon, el agente tomará una acción aleatoria (exploración). Con probabilidad 1 - epsilon, tomará la acción con mayor valor en Q (explotación).

# Función epsilon-greedy
def epsilon_greedy(Q, state, epsilon):
    """
    Esta función implementa la política epsilon-greedy, que balancea la exploración y explotación.
    Con probabilidad epsilon, el agente elige una acción aleatoria (exploración).
    Con probabilidad 1 - epsilon, elige la acción con el mayor valor en la tabla Q (explotación).
    """
    if np.random.rand() < epsilon:  # Si un número aleatorio entre 0 y 1 es menor que epsilon, se elige exploración.
        return np.random.choice(n_actions)  # Exploración: elige una acción aleatoria entre las 2 disponibles.
    else:
        return np.argmax(Q[state])  # Explotación: elige la acción con el valor más alto en la tabla Q para el estado actual.

# Simulación simple de exploración vs. explotación
def exploration_vs_exploitation(Q, epsilon, n_episodes=100):
    """
    Esta función simula una serie de episodios en los que el agente toma decisiones basadas en la política epsilon-greedy.
    Para cada episodio, elige un estado aleatorio y luego toma una acción basándose en la política.
    """
    for _ in range(n_episodes):  # Recorre los episodios.
        state = np.random.randint(0, n_states)  # Selecciona un estado aleatorio entre 0 y 4.
        action = epsilon_greedy(Q, state, epsilon)  # Determina la acción a tomar según la política epsilon-greedy.
        
        # Imprime si la acción tomada fue exploración o explotación según la política epsilon-greedy.
        print(f"Estrategia de acción en estado {state}: {'Exploración' if action != np.argmax(Q[state]) else 'Explotación'}")

# Ejecutamos la simulación de exploración vs explotación
exploration_vs_exploitation(Q, epsilon)  # Llamamos a la función para ver cómo el agente elige acciones basándose en la política.
