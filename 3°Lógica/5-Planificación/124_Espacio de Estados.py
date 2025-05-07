# Representación de un espacio de estados simple
estados = [
    {"cerca_de_meta": False, "recurso": 5},
    {"cerca_de_meta": True, "recurso": 0},
]

def buscar_meta(espacio_estados):
    for estado in espacio_estados:
        if estado["cerca_de_meta"]:
            return estado
    return None

# Búsqueda en el espacio de estados
estado_meta = buscar_meta(estados)
print("Estado meta encontrado:", estado_meta)
