# Importar las bibliotecas necesarias
import numpy as np  # Para operaciones numéricas
import matplotlib.pyplot as plt  # Para graficar

# Crear una imagen de ejemplo (una matriz aleatoria de 256x256)
image = np.random.rand(256, 256)  # Genera una matriz de 256x256 con valores entre 0 y 1

# Simular un filtro Gaussiano simple con numpy (en este caso un filtro promedio 3x3)
kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9  # Filtro promedio (simplificado)
# Convolucionar la imagen con el filtro
filtered_image = np.convolve(image.flatten(), kernel.flatten(), mode='same').reshape(image.shape)

# Mostrar la imagen original y la filtrada
fig, axes = plt.subplots(1, 2, figsize=(10, 5))  # Crear una figura con dos subgráficos
axes[0].imshow(image, cmap='gray')  # Mostrar la imagen original en escala de grises
axes[0].set_title('Imagen Original')  # Título de la imagen original
axes[1].imshow(filtered_image, cmap='gray')  # Mostrar la imagen filtrada en escala de grises
axes[1].set_title('Imagen Filtrada')  # Título de la imagen filtrada
plt.show()  # Mostrar las imágenes

