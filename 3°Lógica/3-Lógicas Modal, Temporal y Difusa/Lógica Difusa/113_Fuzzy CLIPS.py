# -----------------------------------------------
# Base de hechos del sistema difuso
# -----------------------------------------------
hechos = {
    "temperatura": 22,  # Valor de entrada difuso para temperatura
    "humedad": 60       # Valor de entrada difuso para humedad
}

# -----------------------------------------------
# Reglas difusas estilo Fuzzy CLIPS
# -----------------------------------------------
def reglas_difusas():
    temp = hechos["temperatura"]

    # Regla 1: si la temperatura está entre 20 y 25, es confortable
    if 20 <= temp <= 25:
        print("Regla activada: Temperatura confortable")

    # Regla 2: si la humedad es mayor a 50, se considera alta
    if hechos["humedad"] > 50:
        print("Regla activada: Humedad alta")

# -----------------------------------------------
# Ejecución del motor de reglas
# -----------------------------------------------
reglas_difusas()
