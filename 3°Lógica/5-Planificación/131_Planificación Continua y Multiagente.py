# Planificación continua en un sistema multiagente
agentes = {
    "agente1": {"tareas_completadas": False},
    "agente2": {"tareas_completadas": False}
}

def planificacion_multiagente(agentes):
    for agente, estado in agentes.items():
        if not estado["tareas_completadas"]:
            print(f"{agente} ejecutando tareas.")
            estado["tareas_completadas"] = True
        else:
            print(f"{agente} ya completó sus tareas.")

planificacion_multiagente(agentes)
