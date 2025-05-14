# Diccionario que representa una estructura jerárquica de tareas y subtareas.
tareas_jerarquicas = {
    "Tarea Principal": ["Subtarea A", "Subtarea B"],  # La tarea principal tiene dos subtareas.
    "Subtarea A": ["Subtarea A1", "Subtarea A2"],     # Subtarea A tiene dos subtareas.
    "Subtarea B": ["Subtarea B1"],                     # Subtarea B tiene una subtarea.
}

# Función que muestra la jerarquía de tareas y subtareas.
def mostrar_tareas(tareas):
    # Iterar sobre el diccionario de tareas, donde cada clave es una tarea y cada valor es una lista de subtareas.
    for tarea, subtareas in tareas.items():
        # Imprimir el nombre de la tarea y las subtareas correspondientes, unidas por comas.
        print(f"{tarea} tiene las subtareas: {', '.join(subtareas)}")

# Llamada a la función para mostrar las tareas jerárquicas.
mostrar_tareas(tareas_jerarquicas)
