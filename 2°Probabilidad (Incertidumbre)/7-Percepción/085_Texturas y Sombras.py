# Importar las bibliotecas necesarias
import numpy as np  # Para operaciones numéricas y generación de datos aleatorios
import matplotlib.pyplot as plt  # Para graficar y mostrar la imagen

# Generación de una textura con ruido aleatorio
# np.random.rand(256, 256) genera una matriz 256x256 de números aleatorios entre 0 y 1
texture = np.random.rand(256, 256)

# Mostrar la textura generada
# plt.imshow() muestra una matriz como una imagen. 'cmap='gray'' especifica que la imagen será mostrada en escala de grises
plt.imshow(texture, cmap='gray')

# Agregar un título a la imagen
plt.title('Textura Generada')

# Mostrar la figura con la textura generada
plt.show()
