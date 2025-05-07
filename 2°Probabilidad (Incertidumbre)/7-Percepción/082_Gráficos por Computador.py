import matplotlib.pyplot as plt
import numpy as np

# Crear un círculo en el espacio 2D
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

# Crear la figura y el gráfico
plt.figure(figsize=(6,6))
plt.plot(x, y)
plt.title("Gráfico de un Círculo")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
