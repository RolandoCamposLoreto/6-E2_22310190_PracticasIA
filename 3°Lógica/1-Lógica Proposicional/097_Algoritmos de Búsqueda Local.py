# Función objetivo (a minimizar)
def funcion_objetivo(x):
    return x**2 - 4*x + 4

# Búsqueda local
def busqueda_local():
    mejor_x = None
    mejor_valor = float('inf')

    for x in range(-10, 10):
        valor = funcion_objetivo(x)
        if valor < mejor_valor:
            mejor_valor = valor
            mejor_x = x

    return mejor_x, mejor_valor

mejor_x, mejor_valor = busqueda_local()
print(f"Mejor valor encontrado en x = {mejor_x} con valor de la función = {mejor_valor}")
