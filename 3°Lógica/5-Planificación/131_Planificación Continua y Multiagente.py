# Representación de un sistema multiagente, donde cada agente tiene un estado de tareas
agentes = {
    "agente1": {"tareas_completadas": False},  # El agente 1 aún no ha completado sus tareas
    "agente2": {"tareas_completadas": False},  # El agente 2 tampoco ha completado sus tareas
}

# Función que maneja la planificación de tareas en un sistema multiagente
def planificacion_multiagente(agentes):
    # Itera a través de los agentes
    for agente, estado in agentes.items():
        # Si el agente no ha completado sus tareas
        if not estado["tareas_completadas"]:
            print(f"{agente} ejecutando tareas.")  # Se le asigna la ejecución de tareas
            estado["tareas_completadas"] = True  # Marcar las tareas como completadas para ese agente
        else:
            print(f"{agente} ya completó sus tareas.")  # Si ya completó sus tareas, solo se informa

# Llamada a la función para realizar la planificación multiagente
planificacion_multiagente(agentes)
