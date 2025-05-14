# Importar la librería numpy, que es esencial para realizar operaciones matemáticas y manipulaciones de matrices,
# además de trabajar con arrays, álgebra lineal, y funciones matemáticas avanzadas
import numpy as np

# Importar matplotlib.pyplot, que es una herramienta para crear gráficos y visualizaciones en 2D, 
# útil para mostrar imágenes, gráficos y otras representaciones visuales de datos
import matplotlib.pyplot as plt

# Crear una imagen en blanco (de 400x400 píxeles), donde cada píxel tiene 3 valores (RGB) 
# establecidos a 255, lo que corresponde a color blanco
image = np.ones((400, 400, 3), dtype="uint8") * 255

# Dibujar una línea en la imagen, especificando las coordenadas de inicio y fin de la línea
# Se utiliza la función plot de matplotlib, que toma los puntos de inicio y fin
start_point = (50, 50)  # Coordenada de inicio de la línea
end_point = (350, 350)  # Coordenada de fin de la línea
color = (0, 0, 255)  # Color de la línea (rojo en formato BGR)
thickness = 2  # Grosor de la línea

# Usamos plt.plot para dibujar la línea sobre el gráfico, pero no modificamos directamente la imagen aquí
plt.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], color='r', linewidth=2)

# Escribir texto sobre la imagen, especificando las coordenadas y el texto
# Aquí se coloca el texto "Línea Dibujada" en la posición (100, 100) de la imagen
plt.text(100, 100, 'Línea Dibujada', fontsize=12, color='black')

# Finalmente, mostrar la imagen generada con la línea y el texto sobre ella
plt.imshow(image)  # Mostrar la imagen como fondo
plt.title('Imagen con Línea y Etiqueta')  # Título para la ventana del gráfico
plt.show()  # Mostrar el gráfico generado

