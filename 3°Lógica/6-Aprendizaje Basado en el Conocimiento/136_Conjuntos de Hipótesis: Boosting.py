from sklearn.ensemble import GradientBoostingClassifier  # Importa el clasificador de Gradiente Boosting de scikit-learn
import numpy as np  # Importa numpy para manejar matrices y vectores

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5]])  # Características o variables independientes (en este caso, solo una característica numérica)
y = np.array([0, 1, 0, 1, 0])  # Etiquetas de clase correspondientes a cada punto de datos (0 o 1)

# Creación y entrenamiento del modelo de Gradient Boosting
modelo = GradientBoostingClassifier(n_estimators=50, learning_rate=1.0)  # Inicializa el modelo con 50 estimadores y una tasa de aprendizaje de 1.0
modelo.fit(X, y)  # Entrena el modelo con los datos (X como características y y como etiquetas de clase)

# Realizando una predicción para un nuevo valor de X
prediccion = modelo.predict([[6]])  # Predice la clase para un nuevo valor de X=6

# Imprime la predicción
print(f"Predicción para X=6: {prediccion[0]}")  # Muestra el valor predicho para X=6
