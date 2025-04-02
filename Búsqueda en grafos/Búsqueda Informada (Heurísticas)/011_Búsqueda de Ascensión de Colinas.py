def busqueda_ascension_colinas(estado_inicial, estado_objetivo, obtener_heuristica, obtener_vecinos):
    estado_actual = estado_inicial  # Empezamos con el estado inicial
    
    while True:  # Continuamos el proceso hasta encontrar un máximo local
        vecinos = obtener_vecinos(estado_actual)  # Obtener los vecinos del estado actual
        mejor_vecino = None  # Inicializar el mejor vecino
        mejor_heuristica = float('inf')  # Inicializar la heurística del mejor vecino con un valor muy alto
        
        for vecino in vecinos:  # Iterar sobre cada vecino del estado actual
            heuristica = obtener_heuristica(vecino)  # Calcular la heurística del vecino
            if heuristica < mejor_heuristica:  # Si este vecino tiene una heurística mejor (más baja)
                mejor_heuristica = heuristica  # Actualizar la mejor heurística
                mejor_vecino = vecino  # Guardar el vecino como el mejor
                
        if obtener_heuristica(mejor_vecino) >= obtener_heuristica(estado_actual):  # Si no encontramos un vecino con mejor heurística
            return estado_actual  # El estado actual es el óptimo local, terminamos la búsqueda
        
        estado_actual = mejor_vecino  # Actualizamos el estado actual al mejor vecino encontrado
