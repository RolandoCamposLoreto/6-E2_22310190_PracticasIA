# Diccionario que representa las tareas y sus dependencias
tareas = {
    "tarea1": {"predecesores": [], "duracion": 3},  # tarea1 no depende de ninguna otra tarea y tiene una duración de 3 unidades de tiempo.
    "tarea2": {"predecesores": ["tarea1"], "duracion": 2},  # tarea2 depende de tarea1 y tiene una duración de 2 unidades de tiempo.
    "tarea3": {"predecesores": ["tarea2"], "duracion": 1},  # tarea3 depende de tarea2 y tiene una duración de 1 unidad de tiempo.
}

# Función para planificar tareas considerando sus dependencias
def planificar_tareas(tareas):
    orden = []  # Lista para almacenar el orden de las tareas.
    
    # Recorremos todas las tareas en el diccionario.
    for tarea, detalles in tareas.items():
        # Si una tarea no tiene predecesores (es decir, no depende de ninguna tarea), la agregamos al orden de ejecución.
        if not detalles["predecesores"]:
            orden.append(tarea)
    
    # Imprimimos el orden de ejecución de las tareas.
    print("Planificación de tareas:", orden)
    
    # Devolvemos el orden calculado de las tareas.
    return orden

# Llamamos a la función para obtener el orden de las tareas sin considerar sus dependencias posteriores.
planificar_tareas(tareas)
