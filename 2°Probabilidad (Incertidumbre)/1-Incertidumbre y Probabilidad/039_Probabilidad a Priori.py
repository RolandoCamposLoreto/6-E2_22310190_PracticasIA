import numpy as np  # Importamos numpy para trabajar con arreglos de forma eficiente.

# Probabilidades a priori para un dado
probabilidades_a_priori = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])  # Probabilidad uniforme para cada cara del dado

# Mostrar las probabilidades a priori
print("Probabilidades a priori para un dado:")
print(probabilidades_a_priori)  # Imprime las probabilidades de cada cara del dado.

# Ejemplo de uso: Calcular la probabilidad de que salga un número par
# Los números pares en un dado son 2, 4 y 6 (índices 1, 3, 5)
probabilidad_par = np.sum(probabilidades_a_priori[[1, 3, 5]])  # Suma las probabilidades de los índices correspondientes a 2, 4 y 6.

print(f"Probabilidad de que salga un número par: {probabilidad_par}")  # Imprime la probabilidad de que salga un número par.
