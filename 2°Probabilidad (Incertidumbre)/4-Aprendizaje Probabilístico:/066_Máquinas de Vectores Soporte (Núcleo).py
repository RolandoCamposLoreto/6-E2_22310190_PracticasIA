from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
data = load_iris()
X = data.data
y = data.target

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Crear un clasificador SVM
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

# Predicción
y_pred = svm.predict(X_test)

# Evaluación
print(f"Accuracy SVM: {accuracy_score(y_test, y_pred)}")
