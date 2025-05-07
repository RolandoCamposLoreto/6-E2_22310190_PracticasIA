# Probabilidad Condicionada y Normalización - Ejemplo básico

import numpy as np

# Probabilidades de un dado, dado que el resultado es mayor que 3
# Definir la probabilidad conjunta P(A, B) y P(B) para normalización
P_A_given_B = np.array([1/3, 1/3, 1/3])  # P(A|B) es uniforme para caras 4, 5, y 6 de un dado
P_B = np.sum(P_A_given_B)  # P(B) es la probabilidad de que el dado muestre un valor mayor que 3

# Normalización para encontrar P(A|B)
P_A_normalizada = P_A_given_B / P_B

print("Probabilidad condicionada P(A|B) después de normalización:")
print(P_A_normalizada)
