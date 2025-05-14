# Lista de acciones condicionales, cada una con sus condiciones y la acción correspondiente.
acciones = [
    {"condiciones": {"es_dia": True}, "accion": "ir_a_trabajo"},  # Si es de día, la acción es ir al trabajo.
    {"condiciones": {"es_noche": True}, "accion": "descansar"},   # Si es de noche, la acción es descansar.
]

# Función que evalúa las condiciones y ejecuta la acción correspondiente.
def plan_condicional(acciones, condiciones):
    # Recorrer la lista de acciones y evaluar si las condiciones se cumplen.
    for accion in acciones:
        # Verificar que todas las condiciones se cumplan para la acción actual.
        if all(condiciones.get(k) == v for k, v in accion["condiciones"].items()):
            # Si las condiciones se cumplen, imprimir la acción a ejecutar.
            print(f"Acción a ejecutar: {accion['accion']}")

# Llamada a la función plan_condicional con condiciones específicas de "es_dia" y "es_noche".
plan_condicional(acciones, {"es_dia": True, "es_noche": False})
