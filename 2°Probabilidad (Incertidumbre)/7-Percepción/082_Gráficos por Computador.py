import matplotlib.pyplot as plt  # Para graficar
import numpy as np  # Para operaciones numéricas

# Crear un círculo en el espacio 2D utilizando parámetros polares
theta = np.linspace(0, 2*np.pi, 100)  # Genera 100 valores de theta entre 0 y 2*pi
x = np.cos(theta)  # Coordenada x del círculo, coseno de theta
y = np.sin(theta)  # Coordenada y del círculo, seno de theta

# Crear la figura y el gráfico
plt.figure(figsize=(6,6))  # Configura el tamaño de la figura (6x6 pulgadas)
plt.plot(x, y)  # Grafica el círculo (x, y) en el plano 2D
plt.title("Gráfico de un Círculo")  # Título del gráfico
plt.gca().set_aspect('equal', adjustable='box')  # Asegura que el aspecto sea igual (círculo no se distorsiona)
plt.grid(True)  # Activa la cuadrícula en el gráfico
plt.show()  # Muestra el gráfico en pantalla
