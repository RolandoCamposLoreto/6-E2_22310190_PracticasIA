# Importamos la librería NumPy para trabajar con matrices, vectores y operaciones numéricas
import numpy as np

# Definimos la función de activación sigmoide, que aplana cualquier valor entre 0 y 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide, necesaria para retropropagación (gradiente)
def sigmoid_derivative(x):
    return x * (1 - x)

# Conjunto de datos de entrada para el problema XOR (dos entradas binarias)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Salida esperada para cada entrada (la función XOR devuelve 1 si los valores son distintos)
y = np.array([[0], [1], [1], [0]])

# Fijamos la semilla para generar los mismos números aleatorios cada vez que se ejecute el código
np.random.seed(1)

# Tamaños de cada capa de la red neuronal
input_layer_size = 2      # Número de neuronas en la capa de entrada (2 entradas)
hidden_layer_size = 4     # Número de neuronas en la capa oculta
output_layer_size = 1     # Número de neuronas en la capa de salida (salida binaria)

# Inicialización aleatoria de los pesos entre capa de entrada y capa oculta
weights_input_hidden = np.random.rand(input_layer_size, hidden_layer_size)

# Inicialización aleatoria de los pesos entre capa oculta y capa de salida
weights_hidden_output = np.random.rand(hidden_layer_size, output_layer_size)

# Definimos la tasa de aprendizaje, que controla cuánto se ajustan los pesos en cada iteración
learning_rate = 0.1

# Bucle de entrenamiento: se repite 10,000 veces para ajustar los pesos
for epoch in range(10000):
    # --------------------- PROPAGACIÓN HACIA ADELANTE ---------------------
    # Calculamos la entrada a la capa oculta (producto punto entre entradas y pesos)
    hidden_input = np.dot(X, weights_input_hidden)

    # Aplicamos la función de activación a la salida de la capa oculta
    hidden_output = sigmoid(hidden_input)

    # Calculamos la entrada a la capa de salida
    final_input = np.dot(hidden_output, weights_hidden_output)

    # Aplicamos la función de activación para obtener la salida final de la red
    final_output = sigmoid(final_input)

    # --------------------- CÁLCULO DEL ERROR ---------------------
    # Calculamos el error entre la salida esperada y la salida obtenida
    error = y - final_output

    # --------------------- RETROPROPAGACIÓN ---------------------
    # Calculamos el gradiente del error en la salida (derivada de la función de activación)
    d_output = error * sigmoid_derivative(final_output)

    # Calculamos el error propagado hacia la capa oculta
    error_hidden_layer = d_output.dot(weights_hidden_output.T)

    # Calculamos el gradiente del error en la capa oculta
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_output)

    # --------------------- ACTUALIZACIÓN DE PESOS ---------------------
    # Ajustamos los pesos entre capa oculta y salida
    weights_hidden_output += hidden_output.T.dot(d_output) * learning_rate

    # Ajustamos los pesos entre capa de entrada y capa oculta
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

# --------------------- RESULTADOS FINALES ---------------------
# Imprimimos la salida final de la red después del entrenamiento
print("Salida final después de entrenamiento:")
print(final_output)
