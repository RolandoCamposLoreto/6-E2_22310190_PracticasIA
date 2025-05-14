# Importar el modelo de mezcla de gaussianas de sklearn
from sklearn.mixture import GaussianMixture
# Importar la librería numpy para la generación de datos simulados
import numpy as np

# Generación de datos simulados: 100 puntos en un espacio bidimensional (2 características)
X = np.random.rand(100, 2)

# Crear el modelo de mezcla de gaussianas con 2 componentes (distribuciones gaussianas)
model = GaussianMixture(n_components=2)
# Ajustar (entrenar) el modelo con los datos generados
model.fit(X)

# Predecir las etiquetas de los datos generados: el modelo asigna a cada punto uno de los dos componentes (clusters)
labels = model.predict(X)
# Imprimir las etiquetas predichas para cada punto (que indican a qué componente pertenece cada uno)
print(f"Etiquetas predichas: {labels}")
