# Tipos básicos de razonamiento y aprendizaje
def razonamiento_deductivo(factos, regla):
    return regla(factos)

def razonamiento_inductivo(datos):
    modelo = sum(datos) / len(datos)  # Promedio simple
    return modelo

# Ejemplo de razonamiento deductivo
factos = [True, False, True]
regla = lambda hechos: all(hechos)
print("Razonamiento Deductivo:", razonamiento_deductivo(factos, regla))

# Ejemplo de razonamiento inductivo
datos = [1, 2, 3, 4, 5]
print("Modelo Inductivo (Promedio):", razonamiento_inductivo(datos))
