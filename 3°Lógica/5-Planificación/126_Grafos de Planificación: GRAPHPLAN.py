# Diccionario que representa un grafo de planificación, donde las claves son los estados (nodos) 
# y los valores son las tareas disponibles a realizar desde ese estado.
nodos = {
    "Inicio": ["tarea1", "tarea2"],  # Desde el inicio se puede ir a tarea1 o tarea2
    "tarea1": ["tarea3"],  # Después de tarea1, se va a tarea3
    "tarea2": ["tarea3"],  # Después de tarea2, se va a tarea3
    "tarea3": ["Fin"]  # Después de tarea3, se llega al final
}

# Función que simula la planificación de tareas siguiendo el grafo de planificación.
def grafo_planificacion(nodos):
    plan = []  # Lista para almacenar el plan de ejecución de las tareas.
    estado_actual = "Inicio"  # Comienza en el nodo "Inicio".
    
    # Bucle que continuará hasta que se llegue al estado "Fin".
    while estado_actual != "Fin":
        print(f"Estado actual: {estado_actual}")  # Imprime el estado actual de la planificación.
        plan.append(estado_actual)  # Añade el estado actual al plan.
        
        # La siguiente tarea es la primera tarea disponible desde el estado actual.
        estado_actual = nodos[estado_actual][0]  # Elegir la primera tarea disponible desde el nodo actual.
    
    plan.append("Fin")  # Añadimos el estado final al plan de ejecución.
    print("Plan de ejecución:", plan)  # Imprime el plan completo de ejecución.

# Llamada a la función con el grafo de nodos para generar y mostrar el plan de ejecución.
grafo_planificacion(nodos)
