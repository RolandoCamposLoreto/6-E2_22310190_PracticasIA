# Simulación básica estilo Fuzzy CLIPS

hechos = {
    "temperatura": 22,
    "humedad": 60
}

def reglas_difusas():
    temp = hechos["temperatura"]
    if 20 <= temp <= 25:
        print("Regla activada: Temperatura confortable")
    if hechos["humedad"] > 50:
        print("Regla activada: Humedad alta")

reglas_difusas()
