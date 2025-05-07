import numpy as np

# Teorema de Bayes: P(A|B) = P(B|A) * P(A) / P(B)
def bayes_theorem(p_b_a, p_a, p_b):
    return (p_b_a * p_a) / p_b

# Ejemplo
p_b_a = 0.9  # P(B|A)
p_a = 0.5    # P(A)
p_b = 0.7    # P(B)

# Calcular P(A|B)
p_a_b = bayes_theorem(p_b_a, p_a, p_b)
print(f"P(A|B) = {p_a_b}")
