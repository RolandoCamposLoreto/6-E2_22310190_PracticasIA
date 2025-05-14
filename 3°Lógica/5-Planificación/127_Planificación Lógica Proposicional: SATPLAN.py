# Diccionario que representa el estado actual de las proposiciones A y B.
estado = {"A": False, "B": False}

# Lista de acciones disponibles, cada acción tiene precondiciones (condiciones necesarias para que la acción pueda aplicarse)
# y efectos (los cambios que produce la acción en el estado).
acciones = [
    {"precondiciones": {"A": False}, "efectos": {"A": True}},  # Acción que activa A
    {"precondiciones": {"B": False}, "efectos": {"B": True}},  # Acción que activa B
]

# Función que aplica una secuencia de acciones al estado actual.
def aplicar_acciones_plan(estado, acciones):
    plan = []  # Lista donde se almacenarán las acciones que se aplican.
    
    # Iterar sobre cada acción en la lista de acciones.
    for accion in acciones:
        # Comprobar si todas las precondiciones de la acción son verdaderas en el estado actual.
        # Esto se realiza verificando que para cada clave en "precondiciones", el estado tiene el valor correspondiente.
        if all(estado.get(k, False) == v for k, v in accion["precondiciones"].items()):
            estado.update(accion["efectos"])  # Aplicar los efectos de la acción al estado.
            plan.append(accion)  # Añadir la acción al plan si se ha aplicado.
    
    return plan  # Devolver el plan de acciones que fueron ejecutadas.

# Ejecutar las acciones y obtener el plan de ejecución.
plan_ejecutado = aplicar_acciones_plan(estado, acciones)

# Mostrar el estado final después de aplicar las acciones.
print("Estado final después de las acciones:", estado)
