# Lógica temporal simple
# En esta simulación evaluamos la verdad de un hecho en distintos tiempos: pasado, presente y futuro.

# Diccionario que representa el estado del hecho en distintos momentos del tiempo
# 'ayer': el valor del hecho en el pasado
# 'hoy': el valor actual del hecho
# 'mañana': el valor esperado en el futuro (aún no determinado)
historial = {'ayer': True, 'hoy': False, 'mañana': None}

# Función que evalúa si el hecho fue verdadero en el pasado
def fue_verdadero():
    return historial['ayer']

# Función que evalúa si el hecho es verdadero en el presente
def es_verdadero():
    return historial['hoy']

# Función que evalúa si el hecho será verdadero en el futuro
# Aquí usamos None como sinónimo de "aún no se sabe"
def sera_verdadero():
    return historial['mañana']

# Salidas que muestran el valor de verdad del hecho en cada momento del tiempo
print("¿Fue verdadero ayer?:", fue_verdadero())
print("¿Es verdadero hoy?:", es_verdadero())
print("¿Será verdadero mañana?:", sera_verdadero())
