# Importar las librerías necesarias
from sklearn.svm import SVC  # Importar el clasificador SVM
from sklearn.datasets import load_iris  # Cargar el conjunto de datos Iris
from sklearn.model_selection import train_test_split  # Para dividir los datos en entrenamiento y prueba
from sklearn.metrics import accuracy_score  # Para medir la precisión del modelo

# Cargar el conjunto de datos Iris
data = load_iris()  # Cargar el conjunto de datos Iris que ya viene con sklearn
X = data.data  # Características de los datos (mediciones de las flores)
y = data.target  # Etiquetas de las clases (tipos de flores)

# Dividir los datos en entrenamiento y prueba (70% entrenamiento, 30% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Crear un clasificador SVM con kernel lineal
svm = SVC(kernel='linear')  # Creamos el clasificador con un kernel lineal
svm.fit(X_train, y_train)  # Entrenamos el clasificador con los datos de entrenamiento

# Predicción usando los datos de prueba
y_pred = svm.predict(X_test)  # Hacemos predicciones con el modelo entrenado

# Evaluar la precisión del modelo
print(f"Accuracy SVM: {accuracy_score(y_test, y_pred)}")  # Calculamos y mostramos la precisión del modelo
