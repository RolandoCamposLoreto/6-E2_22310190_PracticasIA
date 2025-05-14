# Image: para trabajar con imágenes y crear nuevas imágenes.
# ImageDraw: para dibujar sobre una imagen ya creada.
from PIL import Image, ImageDraw

# Crear una imagen nueva en blanco de tamaño 400x400 píxeles con un fondo blanco (RGB(255, 255, 255))
image = Image.new('RGB', (400, 400), color=(255, 255, 255))

# Crear un objeto ImageDraw que permite dibujar sobre la imagen
draw = ImageDraw.Draw(image)

# Dibujar una línea que simula un movimiento en la imagen, 
# con las coordenadas de inicio (50, 50) y fin (350, 350).
# La línea tiene un color azul (RGB(0, 0, 255)) y un grosor de 2 píxeles.
draw.line([50, 50, 350, 350], fill=(0, 0, 255), width=2)

# Mostrar la imagen generada, que contiene la línea sobre el fondo blanco
image.show()
