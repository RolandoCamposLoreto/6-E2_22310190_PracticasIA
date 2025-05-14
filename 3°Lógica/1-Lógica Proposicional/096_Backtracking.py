# Definimos la función de backtracking, que intenta encontrar una solución
# a un problema asignando valores a las variables en un determinado orden.
def backtracking(solution, variables, index):
    # Si hemos recorrido todas las variables, retornamos la solución encontrada
    if index == len(variables):
        return solution  # Solución encontrada
    
    # Probamos con valores True y False para la variable en la posición actual
    for value in [True, False]:  # Prueba con valores True y False
        solution[index] = value  # Asignamos el valor actual a la variable
        # Llamamos recursivamente a la función para la siguiente variable
        result = backtracking(solution, variables, index + 1)
        # Si se encuentra una solución, la devolvemos
        if result:
            return result  # Si se encuentra una solución, la devuelve

    # Si no se encuentra solución después de probar todos los valores, retornamos None
    return None  # Si no se encuentra solución

# Lista de variables que queremos asignar valores
variables = ['A', 'B', 'C']
# Inicializamos la solución como una lista de None del mismo tamaño que el número de variables
solucion = [None] * len(variables)

# Llamamos a la función de backtracking con la solución inicial, las variables y el índice 0
resultado = backtracking(solucion, variables, 0)

# Imprimimos la solución encontrada
print("Solución encontrada:", resultado)
