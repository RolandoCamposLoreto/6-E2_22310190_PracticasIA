from PIL import Image, ImageDraw

# Crear una imagen en blanco
image = Image.new('RGB', (400, 400), color = (255, 255, 255))
draw = ImageDraw.Draw(image)

# Dibujar un rectángulo como objeto
draw.rectangle([50, 50, 350, 350], outline="black", width=2)

# Mostrar la imagen
image.show()
