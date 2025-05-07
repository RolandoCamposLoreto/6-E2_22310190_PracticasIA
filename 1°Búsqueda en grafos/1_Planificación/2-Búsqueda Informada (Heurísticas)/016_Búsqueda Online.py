def busqueda_online(estado_inicial, obtener_heuristica, obtener_vecinos):
    # Comienza desde el estado inicial
    estado_actual = estado_inicial
    
    while True:
        # Obtiene los vecinos del estado actual
        vecinos = obtener_vecinos(estado_actual)
        
        # Selecciona el vecino con la heurística mínima
        mejor_vecino = min(vecinos, key=obtener_heuristica)
        
        # Si el mejor vecino tiene heurística 0, significa que hemos llegado al objetivo
        if obtener_heuristica(mejor_vecino) == 0:
            return mejor_vecino
        
        # Si no hemos llegado al objetivo, el mejor vecino se convierte en el nuevo estado actual
        estado_actual = mejor_vecino

