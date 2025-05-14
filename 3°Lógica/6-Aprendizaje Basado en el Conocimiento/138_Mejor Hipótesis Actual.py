# Diccionario con las hipótesis y sus métricas de rendimiento (precisión y recall)
hipotesis = {
    "hipotesis_1": {"precision": 0.85, "recall": 0.80},  # Hipótesis 1 con precisión 0.85 y recall 0.80
    "hipotesis_2": {"precision": 0.90, "recall": 0.85},  # Hipótesis 2 con precisión 0.90 y recall 0.85
    "hipotesis_3": {"precision": 0.88, "recall": 0.82},  # Hipótesis 3 con precisión 0.88 y recall 0.82
}

# Seleccionar la mejor hipótesis según la precisión (compara las precisiones de todas las hipótesis)
mejor_hipotesis = max(hipotesis, key=lambda h: hipotesis[h]["precision"])

# Mostrar el nombre de la mejor hipótesis
print(f"La mejor hipótesis es: {mejor_hipotesis}")
