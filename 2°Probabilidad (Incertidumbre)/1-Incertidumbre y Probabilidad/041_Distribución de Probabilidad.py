# Distribución de Probabilidad - Ejemplo básico con una distribución normal

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución normal
mu = 0  # Media
sigma = 1  # Desviación estándar
x = np.linspace(-5, 5, 1000)  # Rango de valores
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)  # PDF normal

# Graficar la distribución de probabilidad
plt.plot(x, y, label="Distribución Normal")
plt.title("Distribución de Probabilidad Normal")
plt.xlabel("Valor")
plt.ylabel("Densidad de Probabilidad")
plt.legend()
plt.show()
