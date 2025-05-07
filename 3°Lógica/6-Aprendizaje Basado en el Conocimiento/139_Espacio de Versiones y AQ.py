# Espacio de versiones y un ejemplo de AQ (Algoritmo de Aprendizaje de Conjuntos)
espacio_versiones = {
    "version_1": {"A": True, "B": False},
    "version_2": {"A": False, "B": True},
}

def comparar_versiones(espacio_versiones):
    version_mejor = None
    for version, valores in espacio_versiones.items():
        if version_mejor is None or valores["A"] > espacio_versiones[version_mejor]["A"]:
            version_mejor = version
    return version_mejor

print("Mejor versión:", comparar_versiones(espacio_versiones))
