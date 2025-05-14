import numpy as np  # Librería para realizar operaciones numéricas y trabajar con arrays
import matplotlib.pyplot as plt  # Librería para generar gráficos

# Definición de los parámetros para la distribución normal
mu = 0  # Media de la distribución
sigma = 1  # Desviación estándar de la distribución

# Generación de un rango de valores para evaluar la distribución
x = np.linspace(-5, 5, 1000)  # Creamos un arreglo de 1000 puntos entre -5 y 5

# Cálculo de la función de densidad de probabilidad (PDF) para la distribución normal
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

# Creación de la gráfica para mostrar la distribución de probabilidad
plt.plot(x, y, label="Distribución Normal")  # Ploteamos los valores de x e y con una etiqueta

# Etiquetas y título para la gráfica
plt.title("Distribución de Probabilidad Normal")  # Título del gráfico
plt.xlabel("Valor")  # Etiqueta en el eje X
plt.ylabel("Densidad de Probabilidad")  # Etiqueta en el eje Y
plt.legend()  # Añadimos una leyenda al gráfico

# Mostrar la gráfica
plt.show()  # Muestra la gráfica generada
