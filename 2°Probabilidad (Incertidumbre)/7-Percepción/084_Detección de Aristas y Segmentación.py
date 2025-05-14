# Importar las bibliotecas necesarias
import numpy as np  # Para operaciones numéricas
import matplotlib.pyplot as plt  # Para graficar

# Crear una imagen de ejemplo (una matriz aleatoria de 256x256)
image = np.random.rand(256, 256)  # Genera una matriz de 256x256 con valores entre 0 y 1

# Crear un filtro Sobel para la detección de bordes
sobel_x = np.array([[-1, 0, 1],  # Filtro Sobel para detección de bordes en la dirección X
                    [-2, 0, 2],
                    [-1, 0, 1]])

sobel_y = np.array([[-1, -2, -1],  # Filtro Sobel para detección de bordes en la dirección Y
                    [0, 0, 0],
                    [1, 2, 1]])

# Aplicar el filtro Sobel en las direcciones X y Y
# Usar convolución para aplicar los filtros a la imagen
image_x = np.convolve(image.flatten(), sobel_x.flatten(), mode='same').reshape(image.shape)  # Aplicar filtro Sobel en dirección X
image_y = np.convolve(image.flatten(), sobel_y.flatten(), mode='same').reshape(image.shape)  # Aplicar filtro Sobel en dirección Y

# Calcular el gradiente total (magnitud) de los bordes usando la fórmula del gradiente
edges = np.sqrt(image_x**2 + image_y**2)  # Magnitud del gradiente: raíz cuadrada de las sumas de los cuadrados de los gradientes X y Y

# Mostrar la imagen original y la detección de bordes
fig, axes = plt.subplots(1, 2, figsize=(10, 5))  # Crear una figura con dos subgráficos
axes[0].imshow(image, cmap='gray')  # Mostrar la imagen original en escala de grises
axes[0].set_title('Imagen Original')  # Título de la imagen original
axes[1].imshow(edges, cmap='gray')  # Mostrar la imagen con los bordes detectados en escala de grises
axes[1].set_title('Detección de Bordes')  # Título de la imagen con los bordes detectados
plt.show()  # Mostrar las imágenes
