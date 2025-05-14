# Importar la librería numpy para operaciones numéricas
import numpy as np

# Datos de ejemplo: secuencia de observaciones (0 o 1 en este caso)
observaciones = np.array([[0], [1], [0], [1], [0]])

# Número de estados ocultos en el modelo de Markov (en este caso, 2 estados)
n_estados = 2

# Inicialización de las matrices del modelo de Markov:
# Matriz de transición: P(E|S) (probabilidad de transición entre estados)
transiciones = np.array([[0.7, 0.3], [0.4, 0.6]])

# Matriz de emisión: P(O|S) (probabilidad de observación dada un estado oculto)
emisiones = np.array([[0.9, 0.1], [0.2, 0.8]])

# Probabilidades iniciales de los estados ocultos: P(S)
inicial = np.array([0.6, 0.4])

# Algoritmo hacia adelante (Forward) para predicción de estados ocultos:
def forward_algorithm(obs, trans, emis, ini):
    n_estados = trans.shape[0]  # Obtener el número de estados a partir de la matriz de transición
    T = len(obs)  # Número de observaciones
    alpha = np.zeros((T, n_estados))  # Matriz de probabilidades hacia adelante (alfa)
    
    # Inicialización: probabilidad del primer estado en función de las observaciones
    alpha[0, :] = ini * emis[:, obs[0]]
    
    # Recursión: calcular las probabilidades hacia adelante para el resto de las observaciones
    for t in range(1, T):
        for j in range(n_estados):
            # Calculamos la probabilidad hacia adelante para el estado j en el tiempo t
            alpha[t, j] = np.dot(alpha[t-1, :], trans[:, j]) * emis[j, obs[t]]
    
    # Normalización: aseguramos que las probabilidades sumen 1 en cada paso de tiempo
    alpha /= alpha.sum(axis=1, keepdims=True)
    return alpha

# Predicción de las probabilidades de los estados ocultos para la secuencia de observaciones
alpha = forward_algorithm(observaciones.flatten(), transiciones, emisiones, inicial)

# Mostrar las probabilidades de los estados ocultos en cada paso de tiempo
print("Probabilidades de estados ocultos: \n", alpha)
