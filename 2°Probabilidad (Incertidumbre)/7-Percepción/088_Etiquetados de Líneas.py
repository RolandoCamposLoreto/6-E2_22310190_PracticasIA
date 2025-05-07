import numpy as np
import matplotlib.pyplot as plt

# Crear una imagen en blanco
image = np.ones((400, 400, 3), dtype="uint8") * 255

# Dibujar una línea
start_point = (50, 50)
end_point = (350, 350)
color = (0, 0, 255)  # Color rojo en BGR
thickness = 2
plt.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], color='r', linewidth=2)

# Escribir texto en la imagen
plt.text(100, 100, 'Línea Dibujada', fontsize=12, color='black')

# Mostrar la imagen
plt.imshow(image)
plt.title('Imagen con Línea y Etiqueta')
plt.show()
