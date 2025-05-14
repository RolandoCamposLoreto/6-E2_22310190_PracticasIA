# Importar la librería numpy para operaciones matemáticas y generación de números aleatorios
import numpy as np
# Importar matplotlib para graficar los resultados
import matplotlib.pyplot as plt

# Generar datos simulados de una distribución normal con media 5 y desviación estándar 2
true_mean = 5  # Media verdadera de la distribución
true_std = 2   # Desviación estándar verdadera de la distribución
data = np.random.normal(true_mean, true_std, 1000)  # Generamos 1000 muestras

# Función de verosimilitud para una distribución normal
# Esta función calcula la verosimilitud de un conjunto de datos dado una media y una desviación estándar
def likelihood(mean, std, data):
    # Calcula la verosimilitud como el producto de las probabilidades de cada muestra
    return np.prod((1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((data - mean) / std)**2))

# Ponderación de verosimilitud
# Creamos un rango de posibles medias para estimar
means = np.linspace(4, 6, 100)  # Generamos 100 valores entre 4 y 6 para la media estimada
# Calculamos la verosimilitud para cada valor de la media
likelihoods = [likelihood(mean, true_std, data) for mean in means]

# Normalización de las verosimilitudes para obtener los pesos
weights = likelihoods / np.sum(likelihoods)

# Graficamos los resultados
plt.plot(means, weights)  # Graficamos los pesos frente a las medias estimadas
plt.title("Ponderación de Verosimilitud")  # Título de la gráfica
plt.xlabel("Media Estimada")  # Etiqueta del eje X
plt.ylabel("Peso")  # Etiqueta del eje Y
plt.show()  # Mostrar la gráfica
