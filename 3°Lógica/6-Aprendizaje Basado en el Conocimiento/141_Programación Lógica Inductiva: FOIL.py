# Implementación simplificada de FOIL (Inducción Lógica)
def foil(datos, reglas_iniciales):
    # Aproximación simple: recorre las reglas iniciales y verifica si se cumplen en los datos
    for regla in reglas_iniciales:
        # Verificar si todos los datos cumplen con la condición de la regla
        if all(dato[regla["atributo"]] == regla["valor"] for dato in datos):
            print(f"Regla '{regla['nombre']}' es válida")  # Si la regla se cumple, se imprime que es válida
            return regla  # Retorna la primera regla que sea válida
    return None  # Si ninguna regla es válida, retorna None

# Datos de ejemplo: lista de diccionarios donde cada diccionario es un conjunto de atributos y su valor
datos = [
    {"color": "rojo", "tamano": "grande", "compra": 1},  # Producto grande y rojo, se compró
    {"color": "verde", "tamano": "pequeno", "compra": 0},  # Producto pequeño y verde, no se compró
]

# Reglas iniciales: lista de reglas con atributos y valores
reglas_iniciales = [
    {"nombre": "Compra si grande", "atributo": "tamano", "valor": "grande"},  # Regla: si el tamaño es grande, se compra
]

# Ejecutar FOIL
print("Regla inducida:", foil(datos, reglas_iniciales))
