def unificar(x, y):
    try:
        if isinstance(x, str) and isinstance(y, str):
            return x == y
        if isinstance(x, tuple) and isinstance(y, tuple):
            return x[0] == y[0] and all(unificar(a, b) for a, b in zip(x[1:], y[1:]))
        return False
    except Exception as e:
        print("Error en unificación:", e)
        return False

# Ejemplo: ama(juan, maria) y ama(X, maria)
print("¿Unifican?", unificar(('ama', 'juan', 'maria'), ('ama', 'X', 'maria')))
