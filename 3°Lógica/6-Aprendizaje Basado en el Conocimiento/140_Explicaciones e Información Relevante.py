# Generar una explicación simple de la predicción
def generar_explicacion(prediccion, datos):
    explicacion = f"La predicción de {prediccion} se basa en los datos {datos}"
    return explicacion

print(generar_explicacion(1, {"edad": 30, "ingresos": 50000}))
