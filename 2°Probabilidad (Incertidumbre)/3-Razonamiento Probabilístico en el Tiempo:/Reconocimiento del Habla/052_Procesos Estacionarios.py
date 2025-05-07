import numpy as np
import matplotlib.pyplot as plt

# Generar datos de un proceso estacionario (distribución normal)
np.random.seed(42)
media = 0
desviacion_estandar = 1
num_muestras = 1000

# Proceso estacionario: Muestras de una normal
proceso = np.random.normal(media, desviacion_estandar, num_muestras)

# Graficar el proceso
plt.plot(proceso)
plt.title('Proceso Estacionario')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.show()
