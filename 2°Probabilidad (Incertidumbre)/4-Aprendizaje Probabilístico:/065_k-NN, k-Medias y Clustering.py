# Importar la librería numpy para operaciones numéricas
import numpy as np

# Función para calcular la distancia Euclidiana entre dos puntos
def distancia(x1, x2):
    """Calcula la distancia Euclidiana entre dos puntos x1 y x2."""
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Algoritmo k-NN (k vecinos más cercanos)
def knn(X_train, y_train, X_test, k=3):
    """
    Algoritmo k-NN para clasificación.
    
    X_train: Datos de entrenamiento (matriz de características).
    y_train: Etiquetas de entrenamiento (vectores de clases).
    X_test: Datos de prueba (puntos a clasificar).
    k: Número de vecinos más cercanos a considerar.
    
    Retorna las predicciones para cada punto de prueba.
    """
    # Lista para almacenar las predicciones
    predicciones = []
    
    # Para cada punto de prueba en X_test
    for test_point in X_test:
        # Calcular las distancias de test_point a todos los puntos de entrenamiento
        distancias = [distancia(test_point, train_point) for train_point in X_train]
        
        # Obtener los índices de los k puntos de entrenamiento más cercanos
        idx_nearest = np.argsort(distancias)[:k]
        
        # Obtener las clases de los k vecinos más cercanos
        vecinos = [y_train[i] for i in idx_nearest]
        
        # Obtener la clase más frecuente entre los vecinos (predicción)
        predicciones.append(np.bincount(vecinos).argmax())
    
    # Convertir las predicciones en un array numpy y devolverlo
    return np.array(predicciones)

# Datos de ejemplo de entrenamiento
X_train = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [6, 7]])
y_train = np.array([0, 0, 1, 1, 1])

# Datos de prueba (puntos a clasificar)
X_test = np.array([[2, 2], [4, 5]])

# Predicción usando el algoritmo k-NN
predicciones = knn(X_train, y_train, X_test, k=3)

# Imprimir las predicciones para los puntos de prueba
print("Predicciones: ", predicciones)
