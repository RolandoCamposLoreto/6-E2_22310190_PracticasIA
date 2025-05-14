# Importar la librería itertools que se usará para generar todas las combinaciones posibles
import itertools

# Definir los operadores lógicos como funciones
# Operador AND: devuelve True si ambos operandos son True
def AND(a, b):
    return a and b

# Operador OR: devuelve True si al menos uno de los operandos es True
def OR(a, b):
    return a or b

# Operador NOT: devuelve el valor opuesto del operando
def NOT(a):
    return not a

# Operador IMPLIES: devuelve False solo si A es True y B es False, es decir, A implica B
def IMPLIES(a, b):
    return not a or b

# Generar todas las combinaciones posibles de los valores de verdad para 2 variables
# itertools.product genera el producto cartesiano de las combinaciones, repitiendo 2 veces False y True
variables = list(itertools.product([False, True], repeat=2))

# Lista para almacenar los resultados de la tabla de verdad
tabla_verdad = []

# Expresión lógica: (A AND B) OR NOT(A)
# Se evalúa la expresión para cada combinación de valores de A y B
for A, B in variables:
    resultado = OR(AND(A, B), NOT(A))  # Ejemplo de expresión lógica combinada
    # Almacenar los valores de A, B y el resultado de la expresión en la tabla de verdad
    tabla_verdad.append((A, B, resultado))

# Mostrar la tabla de verdad con los resultados
print("A\tB\t(A AND B) OR NOT(A)")  # Cabecera
for A, B, resultado in tabla_verdad:
    # Imprimir los valores de A, B y el resultado de la expresión lógica
    print(f"{A}\t{B}\t{resultado}")
