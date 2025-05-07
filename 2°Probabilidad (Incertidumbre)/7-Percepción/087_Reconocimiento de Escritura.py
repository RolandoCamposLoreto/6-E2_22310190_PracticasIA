from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargar el dataset MNIST
mnist = fetch_openml('mnist_784')

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(mnist.data, mnist.target, test_size=0.2, random_state=42)

# Crear un clasificador RandomForest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predecir sobre los datos de prueba
y_pred = clf.predict(X_test)

# Evaluar la precisión
print(f"Precisión: {accuracy_score(y_test, y_pred)}")
