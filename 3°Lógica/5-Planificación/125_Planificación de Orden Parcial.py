# Tareas y dependencias
tareas = {
    "tarea1": {"predecesores": [], "duracion": 3},
    "tarea2": {"predecesores": ["tarea1"], "duracion": 2},
    "tarea3": {"predecesores": ["tarea2"], "duracion": 1},
}

def planificar_tareas(tareas):
    orden = []
    for tarea, detalles in tareas.items():
        if not detalles["predecesores"]:
            orden.append(tarea)
    print("Planificación de tareas:", orden)
    return orden

planificar_tareas(tareas)
