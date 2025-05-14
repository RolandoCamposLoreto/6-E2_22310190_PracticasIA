# Definición de la función de enumeración de inferencia
# Esta función calcula la probabilidad de un evento dado una evidencia utilizando la enumeración en un espacio de probabilidades.
def enumeracion_inferencia(P, evidencia):
    total = 0  # Variable que almacenará la probabilidad total
    # Iteramos sobre todas las posibles configuraciones de probabilidades
    for i in range(len(P)):
        # Comprobamos si la configuración actual de probabilidades coincide con la evidencia proporcionada
        if all(P[i][key] == evidencia[key] for key in evidencia):
            total += P[i]['probabilidad']  # Sumamos la probabilidad de la configuración si coincide con la evidencia
    return total  # Devolvemos la probabilidad total calculada

# Definir el espacio de probabilidades
# En este caso, tenemos una lista de diccionarios donde cada diccionario contiene configuraciones de variables
# como 'Rain' (lluvia), 'Traffic' (tráfico), 'Accident' (accidente) y su probabilidad asociada.
P = [
    {'Rain': 0, 'Traffic': 0, 'Accident': 0, 'probabilidad': 0.5},  # Configuración 1: No lluvia, No tráfico, No accidente
    {'Rain': 1, 'Traffic': 1, 'Accident': 1, 'probabilidad': 0.2},  # Configuración 2: Lluvia, Tráfico, Accidente
    {'Rain': 0, 'Traffic': 1, 'Accident': 0, 'probabilidad': 0.3}   # Configuración 3: No lluvia, Tráfico, No accidente
]

# Definir la evidencia observada
# En este caso, sabemos que está lloviendo y hay tráfico
evidencia = {'Rain': 1, 'Traffic': 1}

# Calcular la probabilidad de un accidente dado la evidencia usando la función de enumeración
prob_accidente = enumeracion_inferencia(P, evidencia)

# Imprimir el resultado
# Mostramos la probabilidad de que haya un accidente dado que se ha observado lluvia y tráfico
print(f"Probabilidad de un accidente dado la evidencia: {prob_accidente:.2f}")
