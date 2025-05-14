# Importar el clasificador Naïve Bayes Gaussiano de sklearn
from sklearn.naive_bayes import GaussianNB
# Importar la función para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.model_selection import train_test_split
# Importar el conjunto de datos Iris de sklearn
from sklearn.datasets import load_iris
# Importar la métrica de precisión (accuracy) para evaluar el rendimiento del modelo
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris, que contiene características de flores y sus respectivas etiquetas (tipos de flores)
data = load_iris()
X = data.data  # Características (mediciones de las flores)
y = data.target  # Etiquetas (tipos de flores)

# Dividir los datos en conjuntos de entrenamiento y prueba. 70% para entrenamiento y 30% para prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Crear el modelo Naïve Bayes Gaussiano
model = GaussianNB()
# Ajustar (entrenar) el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Realizar predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo calculando la precisión (accuracy)
# La precisión se define como el número de predicciones correctas dividido por el número total de predicciones
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
