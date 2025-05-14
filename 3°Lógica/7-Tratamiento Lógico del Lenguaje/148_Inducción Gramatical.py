def induccion_gramatical(ejemplos):
    """
    Realiza inducción gramatical, aprendiendo una estructura basada en ejemplos.
    El proceso consiste en generar reglas de la forma 'A -> B' a partir de las transiciones observadas
    entre palabras consecutivas en los ejemplos dados.
    """
    # Conjunto para almacenar las reglas únicas aprendidas
    reglas = set()

    # Iterar sobre cada ejemplo
    for ejemplo in ejemplos:
        # Separar el ejemplo en palabras
        partes = ejemplo.split()
        
        # Iterar sobre las palabras del ejemplo y generar reglas a partir de las transiciones
        for i in range(len(partes) - 1):
            # Crear la regla en la forma 'A -> B' donde A es la palabra actual y B es la siguiente
            regla = partes[i] + " -> " + partes[i+1]
            # Agregar la regla al conjunto (para evitar duplicados)
            reglas.add(regla)
    
    # Retornar el conjunto de reglas aprendidas
    return reglas

# Ejemplo de cadenas de entrenamiento
ejemplos = ["a b c", "a b d", "a c d"]

# Aprender las reglas de la gramática a partir de los ejemplos
reglas_aprendidas = induccion_gramatical(ejemplos)

# Mostrar las reglas aprendidas
print("Reglas aprendidas:", reglas_aprendidas)  # Salida esperada: {'a -> b', 'b -> c', 'b -> d', 'a -> c'}
