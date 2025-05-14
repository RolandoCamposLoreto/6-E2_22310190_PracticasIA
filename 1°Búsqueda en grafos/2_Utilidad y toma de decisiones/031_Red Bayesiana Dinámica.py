import numpy as np  # Se importa la librería NumPy, que proporciona funciones y estructuras de datos eficientes para operaciones matemáticas, especialmente con arreglos multidimensionales.

# Probabilidades de X1 (estado inicial)
P_X1 = [0.9, 0.1]  # P(X1=0) = 0.9, P(X1=1) = 0.1

# Probabilidades de X2 dado X1 (transición de X1 a X2)
# P(X2=0 | X1=0), P(X2=1 | X1=0)
# P(X2=0 | X1=1), P(X2=1 | X1=1)
P_X2_given_X1 = np.array([[0.8, 0.2],  # Desde X1=0, P(X2=0)=0.8, P(X2=1)=0.2
                           [0.1, 0.9]]) # Desde X1=1, P(X2=0)=0.1, P(X2=1)=0.9

# Función para calcular la probabilidad de X2 dado X1
def calcular_probabilidad_X2(X1_value):
    """
    Calcula las probabilidades de X2 para un valor específico de X1.
    
    Parámetros:
    X1_value (int): El valor de X1 (puede ser 0 o 1).
    
    Devuelve:
    tuple: Probabilidades P(X2=0 | X1) y P(X2=1 | X1).
    """
    # P(X2=0) y P(X2=1) dados X1
    P_X2_0_given_X1 = P_X2_given_X1[X1_value, 0]  # Probabilidad de X2=0 dado X1
    P_X2_1_given_X1 = P_X2_given_X1[X1_value, 1]  # Probabilidad de X2=1 dado X1
    
    return P_X2_0_given_X1, P_X2_1_given_X1

# Supongamos que X1 = 1
X1_value = 1  # Especificamos que el valor de X1 es 1
P_X2_given_X1_1 = calcular_probabilidad_X2(X1_value)  # Calculamos la probabilidad de X2 dado X1=1

# Imprimimos los resultados
print(f"Probabilidad de X2 dado X1={X1_value}:")
print(f"P(X2=0 | X1={X1_value}) = {P_X2_given_X1_1[0]}")  # Probabilidad de X2=0 dado X1=1
print(f"P(X2=1 | X1={X1_value}) = {P_X2_given_X1_1[1]}")  # Probabilidad de X2=1 dado X1=1
