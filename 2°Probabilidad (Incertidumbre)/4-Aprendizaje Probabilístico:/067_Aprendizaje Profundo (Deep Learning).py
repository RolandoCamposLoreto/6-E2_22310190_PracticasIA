# Importamos la librería NumPy para operaciones numéricas y manejo de arreglos
import numpy as np

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la sigmoide para el proceso de retropropagación
def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada para el problema XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas
y = np.array([[0], [1], [1], [0]])              # Salidas deseadas

# Dimensiones de las capas de la red
input_layer_size = 2     # Dos entradas
hidden_layer_size = 2    # Dos neuronas ocultas (mínimo para resolver XOR)
output_layer_size = 1    # Una salida

# Fijamos una semilla para reproducibilidad de resultados
np.random.seed(1)

# Inicialización aleatoria de pesos entre capas
weights_input_hidden = np.random.rand(input_layer_size, hidden_layer_size)  # Pesos de entrada a capa oculta
weights_hidden_output = np.random.rand(hidden_layer_size, output_layer_size)  # Pesos de capa oculta a salida

# Definimos la tasa de aprendizaje
learning_rate = 0.1

# Entrenamiento de la red neuronal
for epoch in range(10000):  # Número de iteraciones (épocas)
    # === Propagación hacia adelante ===
    hidden_input = np.dot(X, weights_input_hidden)       # Suma ponderada para la capa oculta
    hidden_output = sigmoid(hidden_input)                # Activación de la capa oculta

    final_input = np.dot(hidden_output, weights_hidden_output)  # Suma ponderada para la capa de salida
    final_output = sigmoid(final_input)                         # Activación de la capa de salida

    # === Cálculo del error ===
    error = y - final_output  # Diferencia entre la salida esperada y la predicha

    # === Retropropagación ===
    d_output = error * sigmoid_derivative(final_output)         # Gradiente en la capa de salida
    error_hidden_layer = d_output.dot(weights_hidden_output.T)  # Propagamos el error hacia atrás
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_output)  # Gradiente en la capa oculta

    # === Actualización de los pesos ===
    weights_hidden_output += hidden_output.T.dot(d_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

# Mostrar resultados finales
print("Salida final después de entrenamiento:")
print(final_output)
