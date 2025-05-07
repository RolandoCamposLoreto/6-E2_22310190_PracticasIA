# Mejor hipótesis actual en aprendizaje
hipotesis = {
    "hipotesis_1": {"precision": 0.85, "recall": 0.80},
    "hipotesis_2": {"precision": 0.90, "recall": 0.85},
    "hipotesis_3": {"precision": 0.88, "recall": 0.82},
}

# Seleccionar la mejor hipótesis según la precisión
mejor_hipotesis = max(hipotesis, key=lambda h: hipotesis[h]["precision"])
print(f"La mejor hipótesis es: {mejor_hipotesis}")
