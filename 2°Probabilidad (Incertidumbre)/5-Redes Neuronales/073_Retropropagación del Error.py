# Importamos la librería NumPy para manipulación de matrices y operaciones numéricas
import numpy as np

# Definimos la función de activación sigmoide, que convierte los valores de entrada en un rango de 0 a 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # Fórmula de la sigmoide

# Definimos la derivada de la función sigmoide, necesaria para calcular los gradientes durante la retropropagación
def sigmoid_derivative(x):
    return x * (1 - x)  # Derivada de la sigmoide cuando la entrada ya ha pasado por la sigmoide

# ----------------------------------------
# Definimos los datos de entrada y salida esperada para el problema XOR
# Entradas binarias: 2 valores por fila
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Salidas esperadas del problema XOR: 1 salida por fila
y = np.array([[0], [1], [1], [0]])

# ----------------------------------------
# Inicialización aleatoria de pesos para las conexiones entre capas
np.random.seed(1)  # Fijamos una semilla para reproducibilidad de resultados

# Definimos el tamaño de cada capa
input_layer_size = 2       # Dos entradas (X1, X2)
hidden_layer_size = 2      # Dos neuronas en la capa oculta
output_layer_size = 1      # Una sola neurona de salida (0 o 1)

# Pesos entre capa de entrada y capa oculta: matriz de 2x2
weights_input_hidden = np.random.rand(input_layer_size, hidden_layer_size)

# Pesos entre capa oculta y capa de salida: matriz de 2x1
weights_hidden_output = np.random.rand(hidden_layer_size, output_layer_size)

# ----------------------------------------
# Definimos la tasa de aprendizaje que controla el tamaño del paso de actualización
learning_rate = 0.1

# ----------------------------------------
# Entrenamiento del perceptrón multicapa durante 10,000 épocas (iteraciones)
for epoch in range(10000):

    # ------------- Propagación hacia adelante -------------
    # Calculamos la entrada a la capa oculta (producto punto entre entradas y pesos)
    hidden_input = np.dot(X, weights_input_hidden)

    # Aplicamos la función de activación a la salida de la capa oculta
    hidden_output = sigmoid(hidden_input)

    # Calculamos la entrada a la capa de salida
    final_input = np.dot(hidden_output, weights_hidden_output)

    # Aplicamos la función sigmoide a la salida final
    final_output = sigmoid(final_input)

    # ------------- Cálculo del error -------------
    # Error = salida esperada - salida obtenida
    error = y - final_output

    # ------------- Propagación hacia atrás -------------
    # Gradiente de la capa de salida
    d_output = error * sigmoid_derivative(final_output)

    # Calculamos el error de la capa oculta a partir del gradiente de salida y los pesos
    error_hidden_layer = d_output.dot(weights_hidden_output.T)

    # Gradiente de la capa oculta
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_output)

    # ------------- Actualización de pesos -------------
    # Ajustamos los pesos entre capa oculta y salida
    weights_hidden_output += hidden_output.T.dot(d_output) * learning_rate

    # Ajustamos los pesos entre entrada y capa oculta
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

# ----------------------------------------
# Mostramos la salida final de la red después del entrenamiento
print("Salida final después de entrenamiento:")
print(final_output)
