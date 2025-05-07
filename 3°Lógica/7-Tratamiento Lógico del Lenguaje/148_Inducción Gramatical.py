# Inducción gramatical: aprender una gramática a partir de ejemplos

def induccion_gramatical(ejemplos):
    """
    Realiza inducción gramatical, aprendiendo una estructura basada en ejemplos.
    """
    reglas = set()
    for ejemplo in ejemplos:
        partes = ejemplo.split()
        for i in range(len(partes) - 1):
            regla = partes[i] + " -> " + partes[i+1]
            reglas.add(regla)
    return reglas

# Ejemplo de cadena
ejemplos = ["a b c", "a b d", "a c d"]
reglas_aprendidas = induccion_gramatical(ejemplos)
print("Reglas aprendidas:", reglas_aprendidas)  # Salida: {'a -> b', 'b -> c', 'b -> d', 'a -> c'}
