# Lógica de orden superior simple

def es_todo_verdadero(predicado, conjunto):
    return all(predicado(x) for x in conjunto)

# Ejemplo
conjunto = [2, 4, 6, 8]
predicado = lambda x: x % 2 == 0
print("¿Todos son pares?:", es_todo_verdadero(predicado, conjunto))
