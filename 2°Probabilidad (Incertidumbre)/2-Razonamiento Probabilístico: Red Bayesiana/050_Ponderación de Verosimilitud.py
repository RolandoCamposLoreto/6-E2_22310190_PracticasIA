# Ponderación de verosimilitud: Estimar parámetros de una distribución basada en muestras
import numpy as np
import matplotlib.pyplot as plt

# Generar datos simulados de una distribución normal
true_mean = 5
true_std = 2
data = np.random.normal(true_mean, true_std, 1000)

# Función de verosimilitud para una distribución normal
def likelihood(mean, std, data):
    return np.prod((1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((data - mean) / std)**2))

# Ponderación de verosimilitud
means = np.linspace(4, 6, 100)
likelihoods = [likelihood(mean, true_std, data) for mean in means]

# Normalización
weights = likelihoods / np.sum(likelihoods)

# Mostrar resultados
plt.plot(means, weights)
plt.title("Ponderación de Verosimilitud")
plt.xlabel("Media Estimada")
plt.ylabel("Peso")
plt.show()
