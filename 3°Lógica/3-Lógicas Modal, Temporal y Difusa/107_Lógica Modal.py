# Lógica modal simulada
# En lógica modal se trabaja con operadores como "necesariamente" (□) y "posiblemente" (◇)
# Aquí los simulamos con funciones en Python

# La función 'necesario' evalúa si un hecho es necesariamente verdadero
# En este caso, devolvemos True solo si el hecho es estrictamente igual a True
def necesario(hecho):
    return hecho == True

# La función 'posible' evalúa si un hecho es posible, es decir, si su valor es True o False
# Esto simula que algo puede ser posible aunque no sea verdadero (ej: 2 + 2 = 5 es falso, pero es una posibilidad lógica evaluada)
def posible(hecho):
    return hecho in [True, False]

# Evaluamos si la expresión "2 + 2 = 4" es necesariamente verdadera
print("¿Es necesario que 2 + 2 = 4?:", necesario(2 + 2 == 4))

# Evaluamos si la expresión "2 + 2 = 5" es al menos posible (aunque sea falsa)
print("¿Es posible que 2 + 2 = 5?:", posible(2 + 2 == 5))
