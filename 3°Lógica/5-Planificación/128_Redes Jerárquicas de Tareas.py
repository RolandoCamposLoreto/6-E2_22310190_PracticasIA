# Representación jerárquica de tareas
tareas_jerarquicas = {
    "Tarea Principal": ["Subtarea A", "Subtarea B"],
    "Subtarea A": ["Subtarea A1", "Subtarea A2"],
    "Subtarea B": ["Subtarea B1"]
}

def mostrar_tareas(tareas):
    for tarea, subtareas in tareas.items():
        print(f"{tarea} tiene las subtareas: {', '.join(subtareas)}")

mostrar_tareas(tareas_jerarquicas)
