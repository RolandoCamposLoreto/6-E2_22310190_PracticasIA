# Importando la librería numpy para manipulación de matrices y cálculos matemáticos
import numpy as np

# Importando matplotlib para la visualización de gráficos
import matplotlib.pyplot as plt

# Definición de la clase SOM (Mapa Autoorganizado de Kohonen)
class SOM:
    # Constructor de la clase SOM
    def __init__(self, x_size, y_size, input_dim, learning_rate=0.1, sigma=1.0, epochs=100):
        # Tamaño de la red en el eje X
        self.x_size = x_size
        # Tamaño de la red en el eje Y
        self.y_size = y_size
        # Dimensión del vector de entrada
        self.input_dim = input_dim
        # Tasa de aprendizaje
        self.learning_rate = learning_rate
        # Desviación estándar para la vecindad de los nodos
        self.sigma = sigma
        # Número de épocas para el entrenamiento
        self.epochs = epochs
        # Inicialización aleatoria de los pesos de la red
        self.weights = np.random.rand(x_size, y_size, input_dim)
        
    # Método para entrenar el SOM
    def train(self, X):
        # Iteración sobre cada época
        for epoch in range(self.epochs):
            # Iteración sobre cada dato de entrada
            for i in range(X.shape[0]):
                # Seleccionar el vector de entrada
                input_vector = X[i]
                # Calcular las distancias entre los pesos y el vector de entrada
                distances = np.linalg.norm(self.weights - input_vector, axis=2)
                # Encontrar el índice del nodo ganador (el más cercano al punto de entrada)
                winner_idx = np.unravel_index(np.argmin(distances), distances.shape)
                winner_x, winner_y = winner_idx
                
                # Actualizar los pesos de la vecindad alrededor del nodo ganador
                for x in range(self.x_size):
                    for y in range(self.y_size):
                        # Calcular la distancia entre el nodo actual y el nodo ganador
                        distance_to_winner = np.linalg.norm(np.array([x, y]) - np.array([winner_x, winner_y]))
                        # Si la distancia es menor que sigma, el nodo está dentro de la vecindad
                        if distance_to_winner < self.sigma:
                            # Influencia del nodo en función de la distancia
                            influence = np.exp(-distance_to_winner ** 2 / (2 * self.sigma ** 2))
                            # Actualizar los pesos del nodo en la vecindad
                            self.weights[x, y, :] += self.learning_rate * influence * (input_vector - self.weights[x, y, :])

    # Método para obtener los pesos entrenados
    def get_weights(self):
        return self.weights

# Crear un conjunto de datos de ejemplo (100 puntos en 2D)
X = np.random.rand(100, 2)

# Crear y entrenar el mapa autoorganizado de Kohonen con 10x10 nodos
som = SOM(x_size=10, y_size=10, input_dim=2, epochs=100)
som.train(X)

# Visualización de los pesos del mapa después del entrenamiento
plt.imshow(np.mean(som.get_weights(), axis=2), cmap='coolwarm', interpolation='nearest')
# Añadir una barra de color para interpretar la intensidad
plt.colorbar()
# Título del gráfico
plt.title('Mapa Autoorganizado de Kohonen')
# Mostrar el gráfico
plt.show()
