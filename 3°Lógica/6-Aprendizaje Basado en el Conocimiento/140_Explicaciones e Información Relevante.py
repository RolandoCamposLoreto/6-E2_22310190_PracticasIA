# Función para generar una explicación simple de la predicción
def generar_explicacion(prediccion, datos):
    # Se genera una explicación indicando la predicción y los datos utilizados
    explicacion = f"La predicción de {prediccion} se basa en los datos {datos}"
    return explicacion  # Se retorna la explicación generada

# Ejemplo de uso: Generar una explicación para una predicción de "1" basada en los datos proporcionados
print(generar_explicacion(1, {"edad": 30, "ingresos": 50000}))
