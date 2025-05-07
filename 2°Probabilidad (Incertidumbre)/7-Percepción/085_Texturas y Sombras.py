import numpy as np
import matplotlib.pyplot as plt

# Generación de una textura con ruido aleatorio
texture = np.random.rand(256, 256)

# Mostrar la textura generada
plt.imshow(texture, cmap='gray')
plt.title('Textura Generada')
plt.show()
