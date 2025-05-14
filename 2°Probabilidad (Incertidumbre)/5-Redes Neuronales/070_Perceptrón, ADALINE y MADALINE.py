# Importamos la librería NumPy para trabajar con arreglos y operaciones matemáticas
import numpy as np

# Definimos la función de activación escalón (step function)
# Esta función retorna 1 si la entrada es mayor o igual a 0, y 0 en caso contrario
def step_function(x):
    return np.where(x >= 0, 1, 0)

# Creamos la clase Perceptrón que simula una neurona artificial
class Perceptron:
    # Constructor que inicializa pesos aleatorios y la tasa de aprendizaje
    def __init__(self, input_size, learning_rate=0.1):
        # Se suman 1 a los pesos para incluir el sesgo (bias)
        self.weights = np.random.rand(input_size + 1)
        self.learning_rate = learning_rate

    # Método que realiza la predicción para una entrada dada
    def predict(self, inputs):
        # Añadimos el sesgo como un 1 al final de las entradas
        inputs_with_bias = np.append(inputs, 1)
        # Calculamos la suma ponderada (producto punto)
        summation = np.dot(inputs_with_bias, self.weights)
        # Aplicamos la función de activación escalón
        return step_function(summation)

    # Método para entrenar al perceptrón usando el algoritmo de aprendizaje supervisado
    def train(self, X, y, epochs):
        # Repetimos el proceso durante el número de épocas indicado
        for _ in range(epochs):
            for inputs, target in zip(X, y):
                # Realizamos una predicción con los pesos actuales
                prediction = self.predict(inputs)
                # Calculamos el error como la diferencia entre el valor esperado y la predicción
                error = target - prediction
                # Actualizamos los pesos usando la regla del perceptrón
                self.weights += self.learning_rate * error * np.append(inputs, 1)

# Definimos las entradas para el problema XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Definimos las salidas esperadas del problema XOR
y = np.array([0, 1, 1, 0])

# Creamos una instancia del perceptrón con 2 entradas
perceptron = Perceptron(input_size=2)

# Entrenamos el perceptrón con las entradas y salidas durante 100 épocas
perceptron.train(X, y, epochs=100)

# Realizamos predicciones con el modelo entrenado
predictions = [perceptron.predict(x) for x in X]

# Imprimimos las predicciones realizadas
print("Predicciones del Perceptrón: ", predictions)
