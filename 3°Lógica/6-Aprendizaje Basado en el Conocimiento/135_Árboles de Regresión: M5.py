import numpy as np  # Importa la librería numpy para manipulación de arreglos y matrices
from sklearn.tree import DecisionTreeRegressor  # Importa el modelo de árbol de decisión para regresión desde scikit-learn

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5]])  # Características o variables independientes, cada fila es un punto de datos
y = np.array([1.5, 1.7, 2.1, 3.0, 3.2])  # Valores a predecir, correspondientes a cada punto de datos

# Creación y entrenamiento del modelo de árbol de decisión para regresión
modelo = DecisionTreeRegressor()  # Inicializa el modelo de árbol de decisión para regresión
modelo.fit(X, y)  # Entrena el modelo con los datos (X como características y y como valores a predecir)

# Realizando una predicción para un nuevo valor de X
prediccion = modelo.predict([[6]])  # Predice el valor de 'y' para un nuevo valor de X=6

# Imprime la predicción
print(f"Predicción para X=6: {prediccion[0]}")  # Muestra el valor predicho para X=6
