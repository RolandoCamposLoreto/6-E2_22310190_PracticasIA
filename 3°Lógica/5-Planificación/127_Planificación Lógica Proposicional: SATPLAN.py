# Planificación simple usando lógica proposicional
estado = {"A": False, "B": False}
acciones = [
    {"precondiciones": {"A": False}, "efectos": {"A": True}},
    {"precondiciones": {"B": False}, "efectos": {"B": True}},
]

def aplicar_acciones_plan(estado, acciones):
    plan = []
    for accion in acciones:
        if all(estado.get(k, False) == v for k, v in accion["precondiciones"].items()):
            estado.update(accion["efectos"])
            plan.append(accion)
    return plan

plan_ejecutado = aplicar_acciones_plan(estado, acciones)
print("Estado final después de las acciones:", estado)
