# Importamos NumPy para crear arreglos y generar datos numéricos
import numpy as np

# Importamos Matplotlib para graficar las funciones
import matplotlib.pyplot as plt

# === Definición de funciones de activación ===

# Función sigmoide: comprime los valores entre 0 y 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Función tangente hiperbólica: comprime los valores entre -1 y 1
def tanh(x):
    return np.tanh(x)

# Función ReLU (Rectified Linear Unit): salida 0 si x < 0, y x si x >= 0
def relu(x):
    return np.maximum(0, x)

# === Generación del dominio de valores para evaluar las funciones ===
x = np.linspace(-10, 10, 100)  # 100 puntos entre -10 y 10

# === Graficación de las funciones de activación ===
plt.figure(figsize=(10, 6))  # Tamaño de la figura

# Graficar Sigmoid
plt.subplot(3, 1, 1)           # Primera de tres subgráficas (fila 1 de 3)
plt.plot(x, sigmoid(x))       # Dibujar la curva sigmoide
plt.title('Sigmoid')          # Título
plt.grid()                    # Mostrar rejilla

# Graficar Tanh
plt.subplot(3, 1, 2)          # Segunda subgráfica (fila 2 de 3)
plt.plot(x, tanh(x))          # Dibujar tangente hiperbólica
plt.title('Tanh')
plt.grid()

# Graficar ReLU
plt.subplot(3, 1, 3)          # Tercera subgráfica (fila 3 de 3)
plt.plot(x, relu(x))          # Dibujar ReLU
plt.title('ReLU')
plt.grid()

# Ajustar automáticamente los espacios entre subgráficas
plt.tight_layout()

# Mostrar la figura
plt.show()
