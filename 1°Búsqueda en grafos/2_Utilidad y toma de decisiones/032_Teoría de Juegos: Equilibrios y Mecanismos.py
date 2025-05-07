# Teoría de Juegos: Equilibrios y Mecanismos - Ejemplo básico

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Definir el problema de un juego de suma cero (dos jugadores, matriz de pagos)
# Matriz de pagos para dos jugadores en un juego de suma cero
payoffs_player_1 = np.array([[1, -1], [-1, 1]])  # Los pagos del jugador 1 (matriz de pagos)
payoffs_player_2 = -payoffs_player_1  # El pago del jugador 2 es simplemente el negativo del jugador 1

# Definir las estrategias de los jugadores
# Las estrategias están representadas por las probabilidades de elegir cada acción
# En este caso, el jugador 1 tiene dos estrategias y el jugador 2 también tiene dos
x = [0.5, 0.5]  # Probabilidades para el jugador 1 (estrategias 1 y 2)
y = [0.5, 0.5]  # Probabilidades para el jugador 2 (estrategias 1 y 2)

# Resolver el juego usando programación lineal para encontrar el equilibrio de Nash
# Usamos la función linprog de scipy para optimizar las estrategias de los jugadores

# Para el jugador 1, la función de maximización será:
c = [-1, 1]  # Coeficientes de la función objetivo
A = [[-1, 1], [1, -1]]  # Restricciones de las estrategias del jugador 1
b = [0, 0]  # Restricciones del jugador 1
bounds = [(0, 1), (0, 1)]  # Las probabilidades deben estar entre 0 y 1

# Resolver el problema de programación lineal
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# El valor de la función objetivo nos dará el valor esperado del juego
equilibrium_strategy_1 = result.x
equilibrium_value = -result.fun  # El valor es negativo porque estamos maximizando

# Para el jugador 2, las probabilidades se pueden deducir de las probabilidades del jugador 1
equilibrium_strategy_2 = [1 - x for x in equilibrium_strategy_1]

# Mostrar los resultados
print("Equilibrio de Nash:")
print("Estrategias para el jugador 1:", equilibrium_strategy_1)
print("Estrategias para el jugador 2:", equilibrium_strategy_2)
print("Valor del juego:", equilibrium_value)

# Visualizar las estrategias en un gráfico de barras
labels = ['Estrategia 1', 'Estrategia 2']
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].bar(labels, equilibrium_strategy_1, color='b')
ax[0].set_title("Estrategias del Jugador 1")
ax[1].bar(labels, equilibrium_strategy_2, color='r')
ax[1].set_title("Estrategias del Jugador 2")

plt.show()
