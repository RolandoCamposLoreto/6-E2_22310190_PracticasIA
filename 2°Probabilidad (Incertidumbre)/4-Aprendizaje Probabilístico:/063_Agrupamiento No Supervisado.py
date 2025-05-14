# Importar el modelo KMeans de sklearn para hacer agrupamiento
from sklearn.cluster import KMeans
# Importar la librería numpy para la generación de datos simulados
import numpy as np

# Generación de datos simulados: 100 puntos en un espacio bidimensional (2 características)
X = np.random.rand(100, 2)

# Aplicando el algoritmo K-Means para agrupar los datos en 3 clusters
kmeans = KMeans(n_clusters=3)
# Ajustar el modelo K-Means a los datos generados
kmeans.fit(X)

# Predicción de las etiquetas: el modelo asigna a cada punto uno de los tres clusters
labels = kmeans.predict(X)
# Imprimir las etiquetas de agrupamiento para cada punto, indicando a qué cluster pertenece cada uno
print(f"Etiquetas de agrupamiento: {labels}")
