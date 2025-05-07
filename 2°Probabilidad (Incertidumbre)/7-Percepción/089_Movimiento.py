from PIL import Image, ImageDraw

# Crear una imagen en blanco
image = Image.new('RGB', (400, 400), color = (255, 255, 255))
draw = ImageDraw.Draw(image)

# Dibujar un movimiento simulado (línea que se mueve)
draw.line([50, 50, 350, 350], fill=(0, 0, 255), width=2)

# Mostrar la imagen
image.show()
