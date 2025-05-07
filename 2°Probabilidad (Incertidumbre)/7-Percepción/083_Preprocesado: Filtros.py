import numpy as np
import matplotlib.pyplot as plt

# Crear una imagen de ejemplo (una matriz aleatoria de 256x256)
image = np.random.rand(256, 256)

# Simular un filtro Gaussiano simple con numpy
kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9  # Filtro promedio (simplificado)
filtered_image = np.convolve(image.flatten(), kernel.flatten(), mode='same').reshape(image.shape)

# Mostrar la imagen original y la filtrada
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title('Imagen Original')
axes[1].imshow(filtered_image, cmap='gray')
axes[1].set_title('Imagen Filtrada')
plt.show()
