# Función de eliminación de variables
# Esta función elimina una variable específica de las configuraciones de probabilidades y normaliza los resultados
def eliminacion_variables(P, variable):
    # Calcular la probabilidad total sumando las probabilidades donde la variable es igual a 1
    # Filtramos los diccionarios en P donde la variable seleccionada tiene el valor 1
    total_prob = sum([p['probabilidad'] for p in P if p[variable] == 1])
    # Devolvemos la probabilidad total
    return total_prob

# Ejemplo de espacio de probabilidades P
# Este es un espacio discreto con probabilidades asociadas a configuraciones de variables
# 'Rain': lluvia, 'Traffic': tráfico, 'Accident': accidente
P = [
    {'Rain': 0, 'Traffic': 1, 'Accident': 0, 'probabilidad': 0.4},  # No lluvia, Tráfico, No accidente
    {'Rain': 1, 'Traffic': 1, 'Accident': 1, 'probabilidad': 0.5},  # Lluvia, Tráfico, Accidente
    {'Rain': 0, 'Traffic': 0, 'Accident': 0, 'probabilidad': 0.1},  # No lluvia, No tráfico, No accidente
]

# Llamamos a la función de eliminación de variables para calcular la probabilidad total
# Dado que estamos eliminando la variable 'Rain', solo consideramos las configuraciones donde 'Rain' es igual a 1
prob_total = eliminacion_variables(P, 'Rain')

# Imprimimos el resultado de la probabilidad total después de eliminar la variable 'Rain'
print(f"Probabilidad total después de eliminar 'Rain': {prob_total:.2f}")
