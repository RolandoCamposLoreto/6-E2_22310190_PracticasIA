import numpy as np
import matplotlib.pyplot as plt

# Funciones de activación
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

# Generación de valores para graficar
x = np.linspace(-10, 10, 100)

# Graficar funciones de activación
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(x, sigmoid(x))
plt.title('Sigmoid')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(x, tanh(x))
plt.title('Tanh')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(x, relu(x))
plt.title('ReLU')
plt.grid()

plt.tight_layout()
plt.show()
