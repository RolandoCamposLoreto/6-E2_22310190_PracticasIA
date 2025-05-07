import numpy as np
import matplotlib.pyplot as plt

# Generar datos ruidosos
np.random.seed(42)
n = 100
datos = np.sin(np.linspace(0, 10, n)) + np.random.normal(0, 0.5, n)

# Filtrado (suavizado) con una media móvil
def filtro_media_movil(datos, ventana):
    return np.convolve(datos, np.ones(ventana)/ventana, mode='valid')

# Suavizado de los datos
ventana = 5
suavizado = filtro_media_movil(datos, ventana)

# Predicción simple (usando el valor pasado)
predicciones = suavizado[:-1]

# Graficar los resultados
plt.plot(datos, label='Datos Originales')
plt.plot(range(ventana-1, n), suavizado, label='Filtrado (Suavizado)', linestyle='--')
plt.plot(range(ventana-1, n-1), predicciones, label='Predicciones', linestyle=':')
plt.legend()
plt.show()
