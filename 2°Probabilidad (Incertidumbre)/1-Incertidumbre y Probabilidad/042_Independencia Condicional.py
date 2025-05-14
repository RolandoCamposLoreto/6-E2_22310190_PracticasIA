import numpy as np  # Librería para operaciones numéricas y manejo de arrays

# Definir las probabilidades condicionales
P_A_given_B = 0.5  # P(A|B) es la probabilidad de A dado que B ocurre
P_A_given_C = 0.5  # P(A|C) es la probabilidad de A dado que C ocurre

# Si A es independiente de C, entonces P(A|B, C) = P(A|B)
# Esto implica que la probabilidad de A no cambia al conocer C, es decir, P(A|B, C) es igual a P(A|B)
P_A_given_B_and_C = P_A_given_B  # P(A|B,C) = P(A|B) si A es independiente de C

# Mostrar el resultado de la probabilidad condicional bajo la condición de independencia
print(f"Probabilidad condicional P(A|B,C) cuando A es independiente de C: {P_A_given_B_and_C}")