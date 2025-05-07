import numpy as np

# Datos de ejemplo
observaciones = np.array([[0], [1], [0], [1], [0]])

# Número de estados ocultos
n_estados = 2

# Inicialización de matrices de transición, emisión y probabilidad inicial
transiciones = np.array([[0.7, 0.3], [0.4, 0.6]])  # P(E|S)
emisiones = np.array([[0.9, 0.1], [0.2, 0.8]])     # P(O|S)
inicial = np.array([0.6, 0.4])                      # P(S)

# Algoritmo hacia adelante para predicción de estados ocultos
def forward_algorithm(obs, trans, emis, ini):
    n_estados = trans.shape[0]
    T = len(obs)
    alpha = np.zeros((T, n_estados))
    
    # Inicialización
    alpha[0, :] = ini * emis[:, obs[0]]
    
    # Recursión
    for t in range(1, T):
        for j in range(n_estados):
            alpha[t, j] = np.dot(alpha[t-1, :], trans[:, j]) * emis[j, obs[t]]
    
    # Normalización
    alpha /= alpha.sum(axis=1, keepdims=True)
    return alpha

# Predicción de probabilidades de estados ocultos
alpha = forward_algorithm(observaciones.flatten(), transiciones, emisiones, inicial)
print("Probabilidades de estados ocultos: \n", alpha)
