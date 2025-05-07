def backtracking(solution, variables, index):
    if index == len(variables):
        return solution  # Solución encontrada
    
    for value in [True, False]:  # Prueba con valores True y False
        solution[index] = value
        result = backtracking(solution, variables, index + 1)
        if result:
            return result  # Si se encuentra una solución, la devuelve

    return None  # Si no se encuentra solución

variables = ['A', 'B', 'C']
solucion = [None] * len(variables)
resultado = backtracking(solucion, variables, 0)
print("Solución encontrada:", resultado)
