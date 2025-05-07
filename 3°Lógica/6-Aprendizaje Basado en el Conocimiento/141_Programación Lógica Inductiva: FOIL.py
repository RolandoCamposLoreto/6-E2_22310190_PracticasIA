# Implementación simplificada de FOIL (Inducción Lógica)
def foil(datos, reglas_iniciales):
    # Aproximación simple
    for regla in reglas_iniciales:
        if all(dato[regla["atributo"]] == regla["valor"] for dato in datos):
            print(f"Regla '{regla['nombre']}' es válida")
            return regla
    return None

# Datos de ejemplo
datos = [
    {"color": "rojo", "tamano": "grande", "compra": 1},
    {"color": "verde", "tamano": "pequeno", "compra": 0},
]

reglas_iniciales = [
    {"nombre": "Compra si grande", "atributo": "tamano", "valor": "grande"},
]

# Ejecutar FOIL
print("Regla inducida:", foil(datos, reglas_iniciales))
