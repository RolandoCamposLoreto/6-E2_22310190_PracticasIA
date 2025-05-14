# Base de conocimiento simulada en Prolog, donde se almacenan hechos sobre relaciones familiares
base_prolog = {
    'padre': [('juan', 'ana'), ('juan', 'luis')],  # Juan es padre de Ana y Luis
    'madre': [('maria', 'ana')]  # María es madre de Ana
}

# Función para verificar si una persona es padre de otra
def es_padre(padre, hijo):
    # Verifica si la relación padre-hijo existe en la base de conocimiento
    return (padre, hijo) in base_prolog['padre']

# Función para verificar si una persona es madre de otra
def es_madre(madre, hijo):
    # Verifica si la relación madre-hijo existe en la base de conocimiento
    return (madre, hijo) in base_prolog['madre']

# Consultas para comprobar si Juan es padre de Ana y si María es madre de Luis
print("¿Juan es padre de Ana?", es_padre('juan', 'ana'))  # Esperado: True
print("¿María es madre de Luis?", es_madre('maria', 'luis'))  # Esperado: False
