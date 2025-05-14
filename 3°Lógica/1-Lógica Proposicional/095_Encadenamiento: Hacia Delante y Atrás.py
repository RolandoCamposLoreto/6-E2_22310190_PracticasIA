# Base de conocimiento: definimos un diccionario con las variables A y B
# A está en True, y B está en False. Estas variables se utilizarán en los encadenamientos.
base_conocimiento = {
    'A': True,   # Variable A está en True
    'B': False,  # Variable B está en False (inicialmente)
}

def encadenamiento_hacia_adelante():
    try:
        # Verificamos si la variable 'A' existe en la base de conocimiento
        # Usamos base_conocimiento.get() para evitar errores si 'A' falta
        if base_conocimiento.get('A') is not None:
            # Si A es verdadero, realizamos un encadenamiento hacia adelante
            if base_conocimiento['A']:
                # Si A es verdadero, entonces B se establece en True
                base_conocimiento['B'] = True
                print("Encadenamiento hacia adelante: B es verdadero debido a A")
            else:
                print("A no es verdadero, no se puede encadenar hacia adelante.")
        else:
            # Si falta la variable A, lanzamos un error indicando que falta en la base de conocimiento
            raise ValueError("Faltan variables en la base de conocimiento")

    except ValueError as e:
        # Capturamos cualquier error relacionado con la falta de 'A' y lo imprimimos
        print(f"Error en el encadenamiento hacia adelante: {e}")

def encadenamiento_hacia_atras():
    try:
        # Verificamos si la variable 'B' existe en la base de conocimiento
        if base_conocimiento.get('B') is not None:
            # Si B es verdadero, realizamos un encadenamiento hacia atrás
            if base_conocimiento['B']:
                # Si B es verdadero, entonces A se establece en True
                base_conocimiento['A'] = True
                print("Encadenamiento hacia atrás: A es verdadero debido a B")
            else:
                print("B no es verdadero, no se puede encadenar hacia atrás.")
        else:
            # Si falta la variable B, lanzamos un error indicando que falta en la base de conocimiento
            raise ValueError("Faltan variables en la base de conocimiento")

    except ValueError as e:
        # Capturamos cualquier error relacionado con la falta de 'B' y lo imprimimos
        print(f"Error en el encadenamiento hacia atrás: {e}")

# Llamamos a las funciones de encadenamiento hacia adelante y hacia atrás
# Estas funciones modifican la base de conocimiento según las reglas de inferencia
encadenamiento_hacia_adelante()
encadenamiento_hacia_atras()

# Imprimimos la base de conocimiento final después de realizar ambos encadenamientos
print("Base de Conocimiento Final:", base_conocimiento)
