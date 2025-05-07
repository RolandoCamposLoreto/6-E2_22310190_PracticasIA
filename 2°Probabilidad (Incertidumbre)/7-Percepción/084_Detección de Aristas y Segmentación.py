import numpy as np
import matplotlib.pyplot as plt

# Crear una imagen de ejemplo (una matriz aleatoria de 256x256)
image = np.random.rand(256, 256)

# Crear un filtro Sobel simple
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Aplicar el filtro Sobel en las direcciones x y y
image_x = np.convolve(image.flatten(), sobel_x.flatten(), mode='same').reshape(image.shape)
image_y = np.convolve(image.flatten(), sobel_y.flatten(), mode='same').reshape(image.shape)

# Calcular el gradiente total (magnitude)
edges = np.sqrt(image_x**2 + image_y**2)

# Mostrar la imagen original y la detección de bordes
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title('Imagen Original')
axes[1].imshow(edges, cmap='gray')
axes[1].set_title('Detección de Bordes')
plt.show()
