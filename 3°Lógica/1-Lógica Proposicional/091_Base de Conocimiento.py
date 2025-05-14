# Base de conocimiento: un diccionario que contiene hechos sobre las variables A, B, y C.
# En este caso, 'A' es verdadero, 'B' es falso, y 'C' es verdadero.
base_conocimiento = {
    'A': True,
    'B': False,
    'C': True,
}

# Regla de inferencia: Si A es verdadero, entonces B es verdadero.
# Esta regla actualiza la base de conocimiento.
def regla():
    # Comprobamos si el hecho 'A' es verdadero
    if base_conocimiento['A']:
        # Si A es verdadero, entonces actualizamos 'B' a verdadero
        base_conocimiento['B'] = True
        # Imprimimos un mensaje para indicar que B ha cambiado debido a A
        print("B es ahora verdadero debido a A")

# Mostrar la base de conocimiento antes de aplicar la regla
print("Base de Conocimiento Antes:", base_conocimiento)

# Aplicamos la regla de inferencia
regla()

# Mostrar la base de conocimiento después de aplicar la regla
print("Base de Conocimiento Después:", base_conocimiento)
