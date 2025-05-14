import numpy as np  # Importamos la librería numpy para trabajar con arrays y funciones matemáticas
import matplotlib.pyplot as plt  # Importamos matplotlib para graficar los resultados

# Generar datos ruidosos
np.random.seed(42)  # Establecemos una semilla para la reproducibilidad de los resultados
n = 100  # Número de puntos de datos
# Generamos una señal senoidal y le añadimos ruido normal (con media 0 y desviación estándar 0.5)
datos = np.sin(np.linspace(0, 10, n)) + np.random.normal(0, 0.5, n)

# Filtrado (suavizado) con una media móvil
# Función que aplica un filtro de media móvil sobre los datos
def filtro_media_movil(datos, ventana):
    # np.convolve realiza una convolución entre los datos y una ventana de unos, lo que da el suavizado
    return np.convolve(datos, np.ones(ventana)/ventana, mode='valid')

# Suavizado de los datos
ventana = 5  # Definimos el tamaño de la ventana para el filtro de media móvil
suavizado = filtro_media_movil(datos, ventana)  # Aplicamos el filtro sobre los datos

# Predicción simple (usando el valor pasado)
# Usamos los valores suavizados como predicciones, desplazando los datos suavizados para que coincidan con el índice
predicciones = suavizado[:-1]  # Los datos suavizados excluyen el último punto para alinearse con la predicción

# Graficar los resultados
# Graficamos los datos originales, el filtro suavizado y las predicciones
plt.plot(datos, label='Datos Originales')  # Línea de los datos ruidosos
plt.plot(range(ventana-1, n), suavizado, label='Filtrado (Suavizado)', linestyle='--')  # Línea del suavizado
plt.plot(range(ventana-1, n-1), predicciones, label='Predicciones', linestyle=':')  # Línea de las predicciones
plt.legend()  # Añadimos la leyenda a la gráfica
plt.show()  # Mostramos la gráfica
