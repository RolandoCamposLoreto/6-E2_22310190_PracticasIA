import numpy as np  # Librería para operaciones numéricas y manejo de arrays

# Definir las probabilidades
P_A = 0.3  # Probabilidad de A, es decir, la probabilidad de que ocurra el evento A
P_B = 0.4  # Probabilidad de B, es decir, la probabilidad de que ocurra el evento B
P_B_given_A = 0.5  # Probabilidad de B dado A, es decir, la probabilidad de que ocurra B si A ya ha ocurrido

# Aplicar la regla de Bayes: P(A|B) = (P(B|A) * P(A)) / P(B)
# Esta fórmula nos permite calcular la probabilidad de A dado que ha ocurrido B, utilizando las probabilidades de P(B|A), P(A) y P(B)
P_A_given_B = (P_B_given_A * P_A) / P_B

# Mostrar el resultado de la probabilidad condicional P(A|B)
print(f"Probabilidad de A dado B (P(A|B)) usando la regla de Bayes: {P_A_given_B}")