# Función de unificación
def unificar(x, y):
    try:
        # Si ambos son cadenas (strings), la unificación es exitosa si son iguales
        if isinstance(x, str) and isinstance(y, str):
            return x == y
        
        # Si ambos son tuplas (como en el caso de predicados), se comprueba que los primeros elementos coincidan
        # y luego se verifica recursivamente los siguientes elementos de las tuplas.
        if isinstance(x, tuple) and isinstance(y, tuple):
            return x[0] == y[0] and all(unificar(a, b) for a, b in zip(x[1:], y[1:]))  # Recursión sobre el resto de las tuplas
        
        # Si los tipos no coinciden, la unificación falla
        return False
    
    except Exception as e:
        # Si ocurre algún error durante la unificación (por ejemplo, índices fuera de rango)
        print("Error en unificación:", e)
        return False

# Ejemplo: Comparar dos predicados: ama(juan, maria) y ama(X, maria)
# Esto devuelve True si X = juan
print("¿Unifican?", unificar(('ama', 'juan', 'maria'), ('ama', 'X', 'maria')))
