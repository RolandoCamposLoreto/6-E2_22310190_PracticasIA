# Definimos una función de orden superior que recibe:
# - un predicado (una función que retorna True o False)
# - un conjunto (lista de elementos)
# La función evalúa si TODOS los elementos del conjunto satisfacen el predicado
def es_todo_verdadero(predicado, conjunto):
    # Usamos la función 'all' que retorna True solo si todos los elementos del generador son True
    return all(predicado(x) for x in conjunto)

# Definimos un conjunto de números
conjunto = [2, 4, 6, 8]

# Definimos el predicado como una función lambda que verifica si un número es par (x % 2 == 0)
predicado = lambda x: x % 2 == 0

# Llamamos a la función es_todo_verdadero con el conjunto y el predicado, e imprimimos el resultado
# Esto responde a la pregunta: "¿Todos los elementos del conjunto son pares?"
print("¿Todos son pares?:", es_todo_verdadero(predicado, conjunto))
