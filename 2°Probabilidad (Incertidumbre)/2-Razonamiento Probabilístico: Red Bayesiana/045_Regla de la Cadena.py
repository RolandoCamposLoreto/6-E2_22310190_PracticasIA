# La regla de la cadena se usa para descomponer una probabilidad conjunta.
# P(A, B) = P(A|B) * P(B) = P(B|A) * P(A)

P_A_given_B = 0.7  # P(A|B)
P_B = 0.5  # P(B)

# Usamos la regla de la cadena para calcular P(A, B)
P_A_and_B = P_A_given_B * P_B
print(f"P(A, B) = {P_A_and_B}")
