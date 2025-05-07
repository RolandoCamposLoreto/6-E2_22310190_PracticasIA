# Base de conocimiento
base_conocimiento = {
    'A': True,
    'B': False,
}

def encadenamiento_hacia_adelante():
    try:
        if base_conocimiento.get('A') is not None:
            if base_conocimiento['A']:
                base_conocimiento['B'] = True
                print("Encadenamiento hacia adelante: B es verdadero debido a A")
            else:
                print("A no es verdadero, no se puede encadenar hacia adelante.")
        else:
            raise ValueError("Faltan variables en la base de conocimiento")

    except ValueError as e:
        print(f"Error en el encadenamiento hacia adelante: {e}")

def encadenamiento_hacia_atras():
    try:
        if base_conocimiento.get('B') is not None:
            if base_conocimiento['B']:
                base_conocimiento['A'] = True
                print("Encadenamiento hacia atrás: A es verdadero debido a B")
            else:
                print("B no es verdadero, no se puede encadenar hacia atrás.")
        else:
            raise ValueError("Faltan variables en la base de conocimiento")

    except ValueError as e:
        print(f"Error en el encadenamiento hacia atrás: {e}")

# Llamada a las funciones de encadenamiento
encadenamiento_hacia_adelante()
encadenamiento_hacia_atras()
print("Base de Conocimiento Final:", base_conocimiento)
