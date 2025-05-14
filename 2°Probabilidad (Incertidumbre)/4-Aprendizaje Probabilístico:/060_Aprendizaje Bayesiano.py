# Importar la librería numpy que proporciona funciones para cálculos numéricos avanzados
import numpy as np

# Teorema de Bayes: P(A|B) = P(B|A) * P(A) / P(B)
def bayes_theorem(p_b_a, p_a, p_b):
    """
    Aplica el Teorema de Bayes para calcular la probabilidad condicional P(A|B)
    
    Parámetros:
    - p_b_a: Probabilidad de B dado A (P(B|A)), es la probabilidad de que ocurra B si A ya ha ocurrido
    - p_a: Probabilidad de que ocurra A (P(A)), es la probabilidad previa de A
    - p_b: Probabilidad de que ocurra B (P(B)), es la probabilidad previa de B
    
    Retorna:
    - P(A|B): La probabilidad condicional de A dado B, que es el objetivo del teorema
    """
    # Aplicamos la fórmula del Teorema de Bayes: P(A|B) = P(B|A) * P(A) / P(B)
    return (p_b_a * p_a) / p_b  

# Ejemplo de aplicación del Teorema de Bayes

# Definir las probabilidades
p_b_a = 0.9  # P(B|A): Probabilidad de B dado que A ha ocurrido
p_a = 0.5    # P(A): Probabilidad de A (evento inicial)
p_b = 0.7    # P(B): Probabilidad de B (evento observado)

# Calcular la probabilidad condicional P(A|B) utilizando el Teorema de Bayes
p_a_b = bayes_theorem(p_b_a, p_a, p_b)

# Imprimir el resultado calculado de P(A|B)
print(f"P(A|B) = {p_a_b}")
