import numpy as np

# Función de distancia Euclidiana
def distancia(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Algoritmo k-NN
def knn(X_train, y_train, X_test, k=3):
    predicciones = []
    
    for test_point in X_test:
        distancias = [distancia(test_point, train_point) for train_point in X_train]
        idx_nearest = np.argsort(distancias)[:k]
        vecinos = [y_train[i] for i in idx_nearest]
        predicciones.append(np.bincount(vecinos).argmax())
    
    return np.array(predicciones)

# Datos de ejemplo
X_train = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [6, 7]])
y_train = np.array([0, 0, 1, 1, 1])

X_test = np.array([[2, 2], [4, 5]])

# Predicción usando k-NN
predicciones = knn(X_train, y_train, X_test, k=3)
print("Predicciones: ", predicciones)
