# Importamos la librería NumPy para trabajar con arreglos numéricos y operaciones vectorizadas
import numpy as np

# Importamos Matplotlib para realizar gráficos
import matplotlib.pyplot as plt

# Definimos un conjunto de datos 2D que son linealmente separables
# Cada punto es una muestra con dos características (X1, X2)
X = np.array([[2, 3], [1, 6], [7, 8], [6, 5]])

# Etiquetas o clases correspondientes a cada punto (0 o 1)
# Los dos primeros puntos son clase 0, los dos últimos son clase 1
y = np.array([0, 0, 1, 1])

# Visualizamos los datos en un gráfico de dispersión
# Cada punto se pinta con un color diferente según su clase (usando el parámetro 'c=y')
# cmap=plt.cm.RdYlBu indica el mapa de colores que se usa para las clases
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu)

# Título del gráfico
plt.title("Datos Linealmente Separables")

# Etiqueta para el eje X
plt.xlabel("X1")

# Etiqueta para el eje Y
plt.ylabel("X2")

# Mostrar el gráfico en pantalla
plt.show()
