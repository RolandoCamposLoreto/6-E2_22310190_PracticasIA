# Regla de Bayes - Ejemplo básico

import numpy as np

# Definir las probabilidades
P_A = 0.3  # Probabilidad de A
P_B = 0.4  # Probabilidad de B
P_B_given_A = 0.5  # Probabilidad de B dado A

# Aplicar la regla de Bayes: P(A|B) = (P(B|A) * P(A)) / P(B)
P_A_given_B = (P_B_given_A * P_A) / P_B

print(f"Probabilidad de A dado B (P(A|B)) usando la regla de Bayes: {P_A_given_B}")
