import matplotlib.pyplot as plt
import numpy as np

# Definimos una función de utilidad: por ejemplo, una función logarítmica
# que es común en economía para representar aversión al riesgo.
def utilidad_esperada(x):
    return np.log(x)

# Simulamos una serie de valores monetarios
valores = np.linspace(1, 100, 100)  # Valores de 1 a 100

# Calculamos la utilidad para cada valor
utilidades = utilidad_esperada(valores)

# Graficamos la función de utilidad
plt.figure(figsize=(8, 5))
plt.plot(valores, utilidades, label="Función de Utilidad U(x) = log(x)", color='blue')
plt.xlabel("Valor (x)")
plt.ylabel("Utilidad U(x)")
plt.title("Ejemplo de Función de Utilidad")
plt.grid(True)
plt.legend()
plt.show()
