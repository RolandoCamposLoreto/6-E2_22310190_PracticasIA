# Base de conocimiento: diccionario que contiene los valores de las variables A, B, y C.
# En este caso, 'A' es verdadero (True), 'B' es falso (False), y 'C' inicialmente es falso (False).
base_conocimiento = {
    'A': True,
    'B': False,
    'C': False,
}

# Función para realizar la inferencia lógica en la base de conocimiento
def inferencia_logica():
    try:
        # Verificar que las variables 'A' y 'B' existen en la base de conocimiento
        if base_conocimiento.get('A') is not None and base_conocimiento.get('B') is not None:
            # Si A y B son ambos verdaderos, inferimos que C es verdadero
            if base_conocimiento['A'] and base_conocimiento['B']:
                base_conocimiento['C'] = True
                print("Se ha inferido que C es verdadero")
            else:
                # Si A o B no son verdaderos, no se puede inferir C
                print("No se puede inferir C, ya que A y B no son ambos verdaderos.")
        else:
            # Si falta alguna variable en la base de conocimiento, lanzar un error
            raise ValueError("Faltan variables en la base de conocimiento")

    except ValueError as e:
        # Capturar el error y mostrar un mensaje adecuado
        print(f"Error en la inferencia: {e}")

# Llamada a la función de inferencia
inferencia_logica()

# Mostrar la base de conocimiento después de aplicar la inferencia
print("Base de Conocimiento Después de la Inferencia:", base_conocimiento)
