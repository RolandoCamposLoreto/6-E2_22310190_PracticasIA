import numpy as np

# Probabilidades de decisión: 'Acción' (A o B)
probabilidad_accion_A = 0.5
probabilidad_accion_B = 0.5

# Probabilidades de consecuencias dadas la acción tomada
# P(Consecuencia|Acción)
P_consecuencia_given_A = [0.9, 0.1]  # Consecuencias: [Positiva, Negativa] para Acción A
P_consecuencia_given_B = [0.4, 0.6]  # Consecuencias: [Positiva, Negativa] para Acción B

# Cálculo de la probabilidad total de consecuencias (Positiva o Negativa)
P_positiva = probabilidad_accion_A * P_consecuencia_given_A[0] + probabilidad_accion_B * P_consecuencia_given_B[0]
P_negativa = 1 - P_positiva  # Las probabilidades deben sumar 1

print("Probabilidad de Consecuencia Positiva:", P_positiva)
print("Probabilidad de Consecuencia Negativa:", P_negativa)
