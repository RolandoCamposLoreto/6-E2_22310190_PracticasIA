import matplotlib.pyplot as plt  # Importa la librería para crear gráficos
import numpy as np  # Importa la librería para operaciones numéricas, especialmente con arrays

# Definimos una función de utilidad: por ejemplo, una función logarítmica
# que es común en economía para representar aversión al riesgo.
def utilidad_esperada(x):
    return np.log(x)  # Retorna el logaritmo natural del valor 'x'

# Simulamos una serie de valores monetarios
valores = np.linspace(1, 100, 100)  # Genera un array de 100 valores equidistantes entre 1 y 100

# Calculamos la utilidad para cada valor de la serie de valores
utilidades = utilidad_esperada(valores)  # Aplica la función de utilidad a cada valor

# Graficamos la función de utilidad
plt.figure(figsize=(8, 5))  # Define el tamaño de la figura del gráfico
plt.plot(valores, utilidades, label="Función de Utilidad U(x) = log(x)", color='blue')  # Dibuja la gráfica
plt.xlabel("Valor (x)")  # Etiqueta del eje X
plt.ylabel("Utilidad U(x)")  # Etiqueta del eje Y
plt.title("Ejemplo de Función de Utilidad")  # Título del gráfico
plt.grid(True)  # Añade una cuadrícula al gráfico
plt.legend()  # Muestra la leyenda
plt.show()  # Muestra el gráfico
