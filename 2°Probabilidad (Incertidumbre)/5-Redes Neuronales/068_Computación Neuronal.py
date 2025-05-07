import numpy as np

# Función de activación
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide
def sigmoid_derivative(x):
    return x * (1 - x)

# Entrada y salida
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas (XOR)
y = np.array([[0], [1], [1], [0]])  # Salidas esperadas

# Inicialización de pesos
np.random.seed(1)
weights = np.random.rand(X.shape[1], 1)

# Tasa de aprendizaje
learning_rate = 0.1

# Entrenamiento de la neurona
for epoch in range(10000):
    # Propagación hacia adelante
    output = sigmoid(np.dot(X, weights))
    
    # Cálculo del error
    error = y - output
    
    # Propagación hacia atrás (ajuste de pesos)
    adjustments = error * sigmoid_derivative(output)
    weights += np.dot(X.T, adjustments) * learning_rate

# Resultado final
print("Pesos finales: \n", weights)
print("Salida final después de entrenamiento: \n", output)
