# Independencia Condicional - Ejemplo básico

import numpy as np

# Definir las probabilidades condicionales
P_A_given_B = 0.5  # P(A|B)
P_A_given_C = 0.5  # P(A|C)

# Si A es independiente de C, entonces P(A|B, C) = P(A|B)
P_A_given_B_and_C = P_A_given_B  # P(A|B,C) = P(A|B) si A es independiente de C

print(f"Probabilidad condicional P(A|B,C) cuando A es independiente de C: {P_A_given_B_and_C}")
