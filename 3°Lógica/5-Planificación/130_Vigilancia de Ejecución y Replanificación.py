# Ejecución con vigilancia y replanificación
estado = {"tarea_completada": False}

def ejecutar_tarea(estado):
    if not estado["tarea_completada"]:
        print("Ejecutando tarea...")
        estado["tarea_completada"] = True
        print("Tarea completada.")
    else:
        print("La tarea ya está completada, replanificando...")
        # Replanificación
        estado["tarea_completada"] = False
        print("Tarea replanificada.")

ejecutar_tarea(estado)
ejecutar_tarea(estado)
