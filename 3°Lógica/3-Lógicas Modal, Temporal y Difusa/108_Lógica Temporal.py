# Lógica temporal simple

historial = {'ayer': True, 'hoy': False, 'mañana': None}

def fue_verdadero():
    return historial['ayer']

def es_verdadero():
    return historial['hoy']

def sera_verdadero():
    return historial['mañana']

print("¿Fue verdadero ayer?:", fue_verdadero())
print("¿Es verdadero hoy?:", es_verdadero())
print("¿Será verdadero mañana?:", sera_verdadero())
