from sklearn.ensemble import GradientBoostingClassifier
import numpy as np

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5]])  # Características
y = np.array([0, 1, 0, 1, 0])  # Etiquetas

# Aplicando el algoritmo Boosting
modelo = GradientBoostingClassifier(n_estimators=50, learning_rate=1.0)
modelo.fit(X, y)

# Predicción
prediccion = modelo.predict([[6]])  # Predecir para el valor X=6
print(f"Predicción para X=6: {prediccion[0]}")
