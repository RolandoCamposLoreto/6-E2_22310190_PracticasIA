# Función que representa el razonamiento deductivo. La deducción parte de hechos y se aplica una regla.
def razonamiento_deductivo(factos, regla):
    return regla(factos)  # Aplica la regla sobre los hechos proporcionados

# Función que representa el razonamiento inductivo. En este caso, construye un modelo tomando el promedio de los datos.
def razonamiento_inductivo(datos):
    modelo = sum(datos) / len(datos)  # Calcula el promedio de los datos
    return modelo  # Devuelve el modelo

# Ejemplo de razonamiento deductivo
factos = [True, False, True]  # Hechos de ejemplo
# Regla que verifica si todos los hechos son verdaderos (aplicando la función all() para hacer la deducción)
regla = lambda hechos: all(hechos)  
print("Razonamiento Deductivo:", razonamiento_deductivo(factos, regla))  # Imprime el resultado del razonamiento deductivo

# Ejemplo de razonamiento inductivo
datos = [1, 2, 3, 4, 5]  # Datos de ejemplo
print("Modelo Inductivo (Promedio):", razonamiento_inductivo(datos))  # Imprime el modelo inductivo calculado
