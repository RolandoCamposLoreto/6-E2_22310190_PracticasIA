# Estado inicial que indica si la tarea ha sido completada o no
estado = {"tarea_completada": False}

# Función que ejecuta la tarea y maneja la replanificación si es necesario
def ejecutar_tarea(estado):
    # Verificar si la tarea ya ha sido completada
    if not estado["tarea_completada"]:
        # Si la tarea no está completada, ejecutar la tarea
        print("Ejecutando tarea...")
        estado["tarea_completada"] = True  # Marcar la tarea como completada
        print("Tarea completada.")
    else:
        # Si la tarea ya está completada, iniciar replanificación
        print("La tarea ya está completada, replanificando...")
        # Replanificación: volver a marcar la tarea como no completada
        estado["tarea_completada"] = False
        print("Tarea replanificada.")

# Llamada a la función para ejecutar la tarea por primera vez
ejecutar_tarea(estado)

# Llamada a la función para ejecutar la tarea nuevamente, lo que activará la replanificación
ejecutar_tarea(estado)
