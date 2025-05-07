from sklearn.mixture import GaussianMixture
import numpy as np

# Generación de datos simulados
X = np.random.rand(100, 2)

# Modelo de mezcla de gaussianas
model = GaussianMixture(n_components=2)
model.fit(X)

# Predecir las etiquetas de los datos
labels = model.predict(X)
print(f"Etiquetas predichas: {labels}")
