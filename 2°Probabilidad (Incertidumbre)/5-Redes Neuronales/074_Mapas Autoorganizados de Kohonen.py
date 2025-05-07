import numpy as np
import matplotlib.pyplot as plt

class SOM:
    def __init__(self, x_size, y_size, input_dim, learning_rate=0.1, sigma=1.0, epochs=100):
        self.x_size = x_size
        self.y_size = y_size
        self.input_dim = input_dim
        self.learning_rate = learning_rate
        self.sigma = sigma
        self.epochs = epochs
        self.weights = np.random.rand(x_size, y_size, input_dim)
        
    def train(self, X):
        for epoch in range(self.epochs):
            for i in range(X.shape[0]):
                # Encuentra el "ganador" (el nodo más cercano al punto de entrada)
                input_vector = X[i]
                distances = np.linalg.norm(self.weights - input_vector, axis=2)
                winner_idx = np.unravel_index(np.argmin(distances), distances.shape)
                winner_x, winner_y = winner_idx
                
                # Actualiza los pesos de la vecindad
                for x in range(self.x_size):
                    for y in range(self.y_size):
                        distance_to_winner = np.linalg.norm(np.array([x, y]) - np.array([winner_x, winner_y]))
                        if distance_to_winner < self.sigma:
                            influence = np.exp(-distance_to_winner ** 2 / (2 * self.sigma ** 2))
                            self.weights[x, y, :] += self.learning_rate * influence * (input_vector - self.weights[x, y, :])

    def get_weights(self):
        return self.weights

# Crear un conjunto de datos de ejemplo (puntos en 2D)
X = np.random.rand(100, 2)

# Crear y entrenar un mapa autoorganizado de Kohonen
som = SOM(x_size=10, y_size=10, input_dim=2, epochs=100)
som.train(X)

# Visualización de los pesos después del entrenamiento
plt.imshow(np.mean(som.get_weights(), axis=2), cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.title('Mapa Autoorganizado de Kohonen')
plt.show()
