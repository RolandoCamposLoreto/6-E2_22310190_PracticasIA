import numpy as np  # Importamos la librería NumPy para manejar arreglos y operaciones numéricas.
import matplotlib.pyplot as plt  # Importamos Matplotlib para crear gráficos.
from scipy.optimize import linprog  # Importamos la función linprog de SciPy para resolver problemas de programación lineal.

# Definir el problema de un juego de suma cero (dos jugadores, matriz de pagos)
# Matriz de pagos para dos jugadores en un juego de suma cero
payoffs_player_1 = np.array([[1, -1], [-1, 1]])  # Los pagos del jugador 1 (matriz de pagos).
payoffs_player_2 = -payoffs_player_1  # El pago del jugador 2 es simplemente el negativo del jugador 1.

# Definir las estrategias de los jugadores
# Las estrategias están representadas por las probabilidades de elegir cada acción.
# En este caso, el jugador 1 tiene dos estrategias y el jugador 2 también tiene dos.
x = [0.5, 0.5]  # Probabilidades para el jugador 1 (estrategias 1 y 2).
y = [0.5, 0.5]  # Probabilidades para el jugador 2 (estrategias 1 y 2).

# Resolver el juego usando programación lineal para encontrar el equilibrio de Nash
# Usamos la función linprog de scipy para optimizar las estrategias de los jugadores.

# Para el jugador 1, la función de maximización será:
c = [-1, 1]  # Coeficientes de la función objetivo. Negamos la función porque linprog minimiza por defecto.
A = [[-1, 1], [1, -1]]  # Restricciones de las estrategias del jugador 1.
b = [0, 0]  # Restricciones del jugador 1.
bounds = [(0, 1), (0, 1)]  # Las probabilidades deben estar entre 0 y 1 (restricciones sobre las probabilidades).

# Resolver el problema de programación lineal con linprog para encontrar las estrategias óptimas del jugador 1.
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# El valor de la función objetivo nos dará el valor esperado del juego
equilibrium_strategy_1 = result.x  # Estrategias óptimas para el jugador 1.
equilibrium_value = -result.fun  # El valor es negativo porque estamos maximizando, y linprog minimiza.

# Para el jugador 2, las probabilidades se pueden deducir de las probabilidades del jugador 1
equilibrium_strategy_2 = [1 - x for x in equilibrium_strategy_1]  # El jugador 2 toma las probabilidades complementarias.

# Mostrar los resultados
print("Equilibrio de Nash:")
print("Estrategias para el jugador 1:", equilibrium_strategy_1)  # Muestra las estrategias del jugador 1.
print("Estrategias para el jugador 2:", equilibrium_strategy_2)  # Muestra las estrategias del jugador 2.
print("Valor del juego:", equilibrium_value)  # Muestra el valor esperado del juego.

# Visualizar las estrategias en un gráfico de barras
labels = ['Estrategia 1', 'Estrategia 2']  # Etiquetas para las estrategias de los jugadores.
fig, ax = plt.subplots(1, 2, figsize=(10, 5))  # Crea una figura con dos subgráficos.

# Graficar las estrategias del jugador 1
ax[0].bar(labels, equilibrium_strategy_1, color='b')  # Barras para las estrategias del jugador 1 (color azul).
ax[0].set_title("Estrategias del Jugador 1")  # Título del gráfico para el jugador 1.

# Graficar las estrategias del jugador 2
ax[1].bar(labels, equilibrium_strategy_2, color='r')  # Barras para las estrategias del jugador 2 (color rojo).
ax[1].set_title("Estrategias del Jugador 2")  # Título del gráfico para el jugador 2.

# Mostrar el gráfico
plt.show()  # Muestra el gráfico con las estrategias de los dos jugadores.
