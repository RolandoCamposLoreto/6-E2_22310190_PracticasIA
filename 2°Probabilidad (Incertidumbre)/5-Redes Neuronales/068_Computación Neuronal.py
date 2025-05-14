# Importamos NumPy para manejar arreglos y operaciones matemáticas
import numpy as np

# Definimos la función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide, necesaria para retropropagación
def sigmoid_derivative(x):
    return x * (1 - x)

# === Entradas y salidas para el problema XOR ===
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Conjunto de entrada (XOR)
y = np.array([[0], [1], [1], [0]])              # Salidas esperadas

# === Inicialización de los pesos ===
np.random.seed(1)  # Semilla para reproducibilidad
weights = np.random.rand(X.shape[1], 1)  # Pesos aleatorios (2 entradas → 1 salida)

# Tasa de aprendizaje
learning_rate = 0.1

# === Entrenamiento de la red neuronal (una sola neurona) ===
for epoch in range(10000):
    # Propagación hacia adelante
    output = sigmoid(np.dot(X, weights))  # Calcular activación con pesos actuales
    
    # Calcular el error (diferencia entre salida esperada y actual)
    error = y - output
    
    # Ajuste de pesos basado en el error y la derivada de la función sigmoide
    adjustments = error * sigmoid_derivative(output)
    
    # Actualización de pesos usando el gradiente descendente
    weights += np.dot(X.T, adjustments) * learning_rate

# === Resultados después del entrenamiento ===
print("Pesos finales: \n", weights)
print("Salida final después de entrenamiento: \n", output)
