# Importar las bibliotecas necesarias para el procesamiento y la clasificación
from sklearn.datasets import fetch_openml  # Para cargar datasets desde OpenML
from sklearn.model_selection import train_test_split  # Para dividir el dataset en entrenamiento y prueba
from sklearn.ensemble import RandomForestClassifier  # Para usar el clasificador RandomForest
from sklearn.metrics import accuracy_score  # Para evaluar la precisión del modelo

# Cargar el dataset MNIST desde OpenML
mnist = fetch_openml('mnist_784')  # MNIST contiene imágenes de dígitos manuscritos (28x28 píxeles)

# Dividir los datos en un conjunto de entrenamiento (80%) y prueba (20%)
# X_train y X_test contienen las características (pixeles de las imágenes)
# y_train y y_test contienen las etiquetas (dígitos correspondientes)
X_train, X_test, y_train, y_test = train_test_split(mnist.data, mnist.target, test_size=0.2, random_state=42)

# Crear un clasificador RandomForest con 100 árboles
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Entrenar el modelo en los datos de entrenamiento
clf.fit(X_train, y_train)

# Usar el clasificador entrenado para predecir las etiquetas del conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular y mostrar la precisión del modelo en los datos de prueba
# accuracy_score compara las predicciones con las etiquetas reales (y_test)
print(f"Precisión: {accuracy_score(y_test, y_pred)}")
