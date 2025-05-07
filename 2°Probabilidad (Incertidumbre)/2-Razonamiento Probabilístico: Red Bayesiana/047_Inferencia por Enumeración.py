def enumeracion_inferencia(P, evidencia):
    total = 0
    for i in range(len(P)):
        if all(P[i][key] == evidencia[key] for key in evidencia):
            total += P[i]['probabilidad']
    return total

# Definir las probabilidades condicionales
P = [
    {'Rain': 0, 'Traffic': 0, 'Accident': 0, 'probabilidad': 0.5},
    {'Rain': 1, 'Traffic': 1, 'Accident': 1, 'probabilidad': 0.2},
    {'Rain': 0, 'Traffic': 1, 'Accident': 0, 'probabilidad': 0.3}
]

# Definir la evidencia
evidencia = {'Rain': 1, 'Traffic': 1}

# Calcular la probabilidad de un accidente dado la evidencia
prob_accidente = enumeracion_inferencia(P, evidencia)
print(f"Probabilidad de un accidente dado la evidencia: {prob_accidente:.2f}")
