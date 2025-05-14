import numpy as np  # numpy es utilizado para operaciones numéricas y generación de números aleatorios
import matplotlib.pyplot as plt  # matplotlib se utiliza para la creación de gráficos

# Definir parámetros del proceso estacionario
np.random.seed(42)  # Establecer la semilla del generador de números aleatorios para reproducibilidad
media = 0  # Media de la distribución normal
desviacion_estandar = 1  # Desviación estándar de la distribución normal
num_muestras = 1000  # Número de muestras a generar

# Generar un proceso estacionario con una distribución normal
# El proceso estacionario aquí se modela como una serie de 1000 muestras de una normal con media 0 y desviación estándar 1
proceso = np.random.normal(media, desviacion_estandar, num_muestras)

# Graficar el proceso generado
plt.plot(proceso)  # Crear un gráfico de líneas para visualizar la serie temporal
plt.title('Proceso Estacionario')  # Título del gráfico
plt.xlabel('Tiempo')  # Etiqueta del eje X (Tiempo)
plt.ylabel('Valor')  # Etiqueta del eje Y (Valor del proceso)
plt.show()  # Mostrar el gráfico
