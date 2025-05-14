import numpy as np  # Importamos numpy para realizar operaciones matemáticas eficientes con matrices.

# Función para calcular la entropía (medida de incertidumbre)
def entropia(probabilidades):
    # La entropía se calcula como la suma de -p * log2(p) para cada probabilidad p
    return -np.sum(probabilidades * np.log2(probabilidades))  # Usamos np.log2 para calcular el logaritmo en base 2

# Ejemplo: distribución de probabilidades de un dado
probabilidades = np.ones(6) / 6  # Probabilidad uniforme para un dado (cada cara tiene 1/6 de probabilidad)
h = entropia(probabilidades)  # Calculamos la entropía de esta distribución.

print(f"Incertidumbre (Entropía) de un dado: {h} bits")  # Mostramos el valor de la entropía en bits.
