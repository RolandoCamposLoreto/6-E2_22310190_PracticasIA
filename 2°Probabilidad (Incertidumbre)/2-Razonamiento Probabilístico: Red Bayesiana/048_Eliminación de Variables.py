def eliminacion_variables(P, variable):
    # Eliminar la variable de las probabilidades y normalizar
    total_prob = sum([p['probabilidad'] for p in P if p[variable] == 1])
    return total_prob

# Ejemplo de probabilidades
P = [
    {'Rain': 0, 'Traffic': 1, 'Accident': 0, 'probabilidad': 0.4},
    {'Rain': 1, 'Traffic': 1, 'Accident': 1, 'probabilidad': 0.5},
    {'Rain': 0, 'Traffic': 0, 'Accident': 0, 'probabilidad': 0.1},
]

# Eliminar la variable 'Rain' y calcular la probabilidad total
prob_total = eliminacion_variables(P, 'Rain')
print(f"Probabilidad total después de eliminar 'Rain': {prob_total:.2f}")
