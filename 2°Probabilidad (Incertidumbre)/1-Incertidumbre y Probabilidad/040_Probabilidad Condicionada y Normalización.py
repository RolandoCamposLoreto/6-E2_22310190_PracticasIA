import numpy as np  # Importa la librería NumPy para manejar arrays y operaciones matemáticas

# Probabilidades de un dado, dado que el resultado es mayor que 3
# P(A|B) es la probabilidad de que el dado muestre una cara específica (4, 5, o 6),
# dado que ya sabemos que el resultado es mayor que 3 (evento B).
P_A_given_B = np.array([1/3, 1/3, 1/3])  # Asigna una probabilidad uniforme para las caras 4, 5 y 6

# Calcula P(B), que es la probabilidad de que el dado muestre un valor mayor que 3.
# Como las caras mayores que 3 son 4, 5 y 6, P(B) es la suma de las probabilidades de esas caras.
P_B = np.sum(P_A_given_B)  # Suma las probabilidades de las caras 4, 5 y 6 (0.33 + 0.33 + 0.33)

# Normaliza P(A|B) para encontrar la probabilidad condicionada, dividiendo por P(B).
# La normalización asegura que la suma de las probabilidades sea 1.
P_A_normalizada = P_A_given_B / P_B  # Divide cada valor de P(A|B) por P(B) para normalizar

# Imprime la probabilidad condicionada P(A|B) después de la normalización
print("Probabilidad condicionada P(A|B) después de normalización:")
print(P_A_normalizada)  # Muestra los valores de la probabilidad normalizada
