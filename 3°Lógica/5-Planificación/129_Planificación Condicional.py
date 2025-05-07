# Planificación con condiciones
acciones = [
    {"condiciones": {"es_dia": True}, "accion": "ir_a_trabajo"},
    {"condiciones": {"es_noche": True}, "accion": "descansar"},
]

def plan_condicional(acciones, condiciones):
    for accion in acciones:
        if all(condiciones.get(k) == v for k, v in accion["condiciones"].items()):
            print(f"Acción a ejecutar: {accion['accion']}")

plan_condicional(acciones, {"es_dia": True, "es_noche": False})
