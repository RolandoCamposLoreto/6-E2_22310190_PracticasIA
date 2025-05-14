import numpy as np  # Importa la librería NumPy, que proporciona soporte para operaciones numéricas y arrays.

# Probabilidades de decisión: 'Acción' (A o B)
probabilidad_accion_A = 0.5  # La probabilidad de tomar la Acción A es 0.5 (50%)
probabilidad_accion_B = 0.5  # La probabilidad de tomar la Acción B es 0.5 (50%)

# Probabilidades de consecuencias dadas la acción tomada
# P(Consecuencia|Acción)
P_consecuencia_given_A = [0.9, 0.1]  # Consecuencias para Acción A: [Positiva (90%), Negativa (10%)]
P_consecuencia_given_B = [0.4, 0.6]  # Consecuencias para Acción B: [Positiva (40%), Negativa (60%)]

# Cálculo de la probabilidad total de consecuencias (Positiva o Negativa)
P_positiva = probabilidad_accion_A * P_consecuencia_given_A[0] + probabilidad_accion_B * P_consecuencia_given_B[0]
# La probabilidad total de una consecuencia positiva es la probabilidad de cada acción multiplicada por la probabilidad de obtener una consecuencia positiva dada la acción.

P_negativa = 1 - P_positiva  # La probabilidad de una consecuencia negativa es el complemento de la probabilidad positiva.

print("Probabilidad de Consecuencia Positiva:", P_positiva)  # Muestra la probabilidad de una consecuencia positiva
print("Probabilidad de Consecuencia Negativa:", P_negativa)  # Muestra la probabilidad de una consecuencia negativa
