import numpy as np

# Probabilidades de X1 (estado inicial)
P_X1 = [0.9, 0.1]  # P(X1=0) = 0.9, P(X1=1) = 0.1

# Probabilidades de X2 dado X1 (transición de X1 a X2)
P_X2_given_X1 = np.array([[0.8, 0.2],  # P(X2=0 | X1=0), P(X2=1 | X1=0)
                           [0.1, 0.9]]) # P(X2=0 | X1=1), P(X2=1 | X1=1)

# Función para calcular la probabilidad de X2 dado X1
def calcular_probabilidad_X2(X1_value):
    # P(X2=0) y P(X2=1) dados X1
    P_X2_0_given_X1 = P_X2_given_X1[X1_value, 0]
    P_X2_1_given_X1 = P_X2_given_X1[X1_value, 1]
    
    return P_X2_0_given_X1, P_X2_1_given_X1

# Supongamos que X1 = 1
X1_value = 1
P_X2_given_X1_1 = calcular_probabilidad_X2(X1_value)

print(f"Probabilidad de X2 dado X1={X1_value}:")
print(f"P(X2=0 | X1={X1_value}) = {P_X2_given_X1_1[0]}")
print(f"P(X2=1 | X1={X1_value}) = {P_X2_given_X1_1[1]}")
