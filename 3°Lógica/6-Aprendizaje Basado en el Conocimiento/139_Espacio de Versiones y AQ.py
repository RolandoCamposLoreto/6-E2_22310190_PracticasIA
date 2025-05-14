# Diccionario que representa un espacio de versiones con diferentes combinaciones de valores para "A" y "B"
espacio_versiones = {
    "version_1": {"A": True, "B": False},  # Versión 1 tiene A=True, B=False
    "version_2": {"A": False, "B": True},  # Versión 2 tiene A=False, B=True
}

# Función que compara las versiones según un criterio (en este caso, el valor de "A")
def comparar_versiones(espacio_versiones):
    version_mejor = None  # Inicializar la variable que almacenará la mejor versión
    for version, valores in espacio_versiones.items():  # Iterar sobre cada versión y sus valores asociados
        # Si no hay una versión mejor aún o la versión actual tiene un valor "A" mayor, actualizar la mejor versión
        if version_mejor is None or valores["A"] > espacio_versiones[version_mejor]["A"]:
            version_mejor = version  # Asignar la versión actual como la mejor
    return version_mejor  # Retornar la versión con el valor "A" más alto

# Imprimir el nombre de la mejor versión basada en el valor de "A"
print("Mejor versión:", comparar_versiones(espacio_versiones))
