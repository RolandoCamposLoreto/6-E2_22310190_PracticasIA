# Incertidumbre - Ejemplo básico utilizando la entropía como medida de incertidumbre

import numpy as np

# Función para calcular la entropía (medida de incertidumbre)
def entropia(probabilidades):
    # La entropía se calcula como la suma de -p * log2(p) para cada probabilidad p
    return -np.sum(probabilidades * np.log2(probabilidades))

# Ejemplo: distribución de probabilidades de un dado
probabilidades = np.ones(6) / 6  # Probabilidad uniforme para un dado
h = entropia(probabilidades)

print(f"Incertidumbre (Entropía) de un dado: {h} bits")
