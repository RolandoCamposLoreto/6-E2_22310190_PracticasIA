# Definimos la función objetivo que queremos minimizar
# Esta función es un polinomio de segundo grado: f(x) = x^2 - 4x + 4
def funcion_objetivo(x):
    return x**2 - 4*x + 4

# Implementación de búsqueda local para encontrar el valor mínimo de la función
def busqueda_local():
    mejor_x = None  # Variable para almacenar el valor de x que da el mejor resultado
    mejor_valor = float('inf')  # Inicializamos el mejor valor como infinito

    # Probamos diferentes valores de x en el rango de -10 a 9
    # Aquí estamos buscando el mínimo en el intervalo [−10, 10)
    for x in range(-10, 10):
        valor = funcion_objetivo(x)  # Calculamos el valor de la función en x
        # Si el valor calculado es mejor (más bajo) que el mejor valor encontrado hasta ahora
        if valor < mejor_valor:
            mejor_valor = valor  # Actualizamos el mejor valor
            mejor_x = x  # Actualizamos el valor de x que produce el mejor valor

    return mejor_x, mejor_valor  # Retornamos el mejor x y su valor correspondiente

# Ejecutamos la búsqueda local para encontrar el mejor valor de x y su valor en la función
mejor_x, mejor_valor = busqueda_local()

# Mostramos el mejor valor encontrado en el rango de x
print(f"Mejor valor encontrado en x = {mejor_x} con valor de la función = {mejor_valor}")

