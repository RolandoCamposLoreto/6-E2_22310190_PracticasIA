import numpy as np
from sklearn.tree import DecisionTreeRegressor

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5]])  # Características
y = np.array([1.5, 1.7, 2.1, 3.0, 3.2])  # Valores a predecir

# Entrenando un árbol de regresión M5 (Usando sklearn)
modelo = DecisionTreeRegressor()
modelo.fit(X, y)

# Predicción
prediccion = modelo.predict([[6]])  # Predecir para el valor X=6
print(f"Predicción para X=6: {prediccion[0]}")
