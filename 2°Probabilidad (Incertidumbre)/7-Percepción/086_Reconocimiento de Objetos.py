# Importar las bibliotecas necesarias
from PIL import Image, ImageDraw  # Importa la biblioteca PIL (Pillow) para crear y manipular imágenes

# Crear una nueva imagen en blanco (de 400x400 píxeles) en el espacio de color RGB
# El color blanco está representado por (255, 255, 255) en el modelo RGB
image = Image.new('RGB', (400, 400), color = (255, 255, 255))

# Crear un objeto 'draw' que permitirá dibujar sobre la imagen
draw = ImageDraw.Draw(image)

# Dibujar un rectángulo en la imagen
# Las coordenadas [50, 50, 350, 350] especifican la esquina superior izquierda (50, 50) 
# y la esquina inferior derecha (350, 350) del rectángulo
# El parámetro 'outline' especifica el color del borde del rectángulo (negro)
# El parámetro 'width' establece el grosor del borde
draw.rectangle([50, 50, 350, 350], outline="black", width=2)

# Mostrar la imagen generada
image.show()

