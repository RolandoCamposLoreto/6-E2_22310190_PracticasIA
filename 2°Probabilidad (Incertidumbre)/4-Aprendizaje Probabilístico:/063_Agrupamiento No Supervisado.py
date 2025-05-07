from sklearn.cluster import KMeans
import numpy as np

# Generación de datos simulados
X = np.random.rand(100, 2)

# Aplicando K-Means
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Predicción de etiquetas
labels = kmeans.predict(X)
print(f"Etiquetas de agrupamiento: {labels}")
