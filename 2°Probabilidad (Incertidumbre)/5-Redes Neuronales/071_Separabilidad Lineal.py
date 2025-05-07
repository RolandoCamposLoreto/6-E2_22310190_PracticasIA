import numpy as np
import matplotlib.pyplot as plt

# Datos linealmente separables
X = np.array([[2, 3], [1, 6], [7, 8], [6, 5]])
y = np.array([0, 0, 1, 1])  # 0 y 1 son las clases

# Visualización de los datos
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu)
plt.title("Datos Linealmente Separables")
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()
