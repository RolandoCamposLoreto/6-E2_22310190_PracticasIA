import numpy as np

# Función de activación (función escalón)
def step_function(x):
    return np.where(x >= 0, 1, 0)

# Perceptrón
class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.random.rand(input_size + 1)  # Pesos y sesgo
        self.learning_rate = learning_rate

    def predict(self, inputs):
        inputs_with_bias = np.append(inputs, 1)  # Añadir el sesgo
        summation = np.dot(inputs_with_bias, self.weights)
        return step_function(summation)

    def train(self, X, y, epochs):
        for _ in range(epochs):
            for inputs, target in zip(X, y):
                prediction = self.predict(inputs)
                error = target - prediction
                self.weights += self.learning_rate * error * np.append(inputs, 1)

# Datos de entrenamiento para XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Entrenamiento del perceptrón
perceptron = Perceptron(input_size=2)
perceptron.train(X, y, epochs=100)

# Predicciones
predictions = [perceptron.predict(x) for x in X]
print("Predicciones del Perceptrón: ", predictions)
