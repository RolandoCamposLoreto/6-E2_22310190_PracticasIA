# Representación de un grafo de planificación simple
nodos = {
    "Inicio": ["tarea1", "tarea2"],
    "tarea1": ["tarea3"],
    "tarea2": ["tarea3"],
    "tarea3": ["Fin"]
}

def grafo_planificacion(nodos):
    plan = []
    estado_actual = "Inicio"
    while estado_actual != "Fin":
        print(f"Estado actual: {estado_actual}")
        plan.append(estado_actual)
        estado_actual = nodos[estado_actual][0]  # Elegir la primera tarea disponible
    plan.append("Fin")
    print("Plan de ejecución:", plan)

grafo_planificacion(nodos)
