import itertools

# Definir los operadores lógicos
def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def IMPLIES(a, b):
    return not a or b

# Generar todas las combinaciones posibles de los valores de verdad para 2 variables
variables = list(itertools.product([False, True], repeat=2))
tabla_verdad = []

# Expresión lógica: (A AND B) OR NOT(A)
for A, B in variables:
    resultado = OR(AND(A, B), NOT(A))  # Ejemplo de expresión
    tabla_verdad.append((A, B, resultado))

# Mostrar la tabla de verdad
print("A\tB\t(A AND B) OR NOT(A)")
for A, B, resultado in tabla_verdad:
    print(f"{A}\t{B}\t{resultado}")
