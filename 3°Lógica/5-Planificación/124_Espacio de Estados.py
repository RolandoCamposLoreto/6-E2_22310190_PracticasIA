# Representación de un espacio de estados simple
# Cada estado es un diccionario que representa una situación con las claves 'cerca_de_meta' y 'recurso'.
estados = [
    {"cerca_de_meta": False, "recurso": 5},  # Estado 1: No cerca de la meta, con 5 recursos.
    {"cerca_de_meta": True, "recurso": 0},   # Estado 2: Cerca de la meta, con 0 recursos.
]

# Función para buscar el estado meta en el espacio de estados
def buscar_meta(espacio_estados):
    # Recorremos todos los estados en el espacio de estados.
    for estado in espacio_estados:
        # Si el estado tiene la clave 'cerca_de_meta' con valor True, lo devolvemos.
        if estado["cerca_de_meta"]:
            return estado
    # Si no encontramos un estado meta, devolvemos None.
    return None

# Búsqueda en el espacio de estados
estado_meta = buscar_meta(estados)

# Imprimimos el resultado de la búsqueda, que es el estado meta si se encuentra, o None si no se encuentra.
print("Estado meta encontrado:", estado_meta)
