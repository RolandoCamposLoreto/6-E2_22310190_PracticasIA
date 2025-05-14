def busqueda_tabu(estado_inicial, obtener_heuristica, obtener_vecinos, max_iteraciones=100): # Función que realiza búsqueda tabú con heurística, vecinos y límite de iteraciones.
    estado_actual = estado_inicial  # Comenzamos con el estado inicial
    tabu_list = set()  # Inicializamos la lista Tabú, que evitará regresar a ciertos estados

    for _ in range(max_iteraciones):  # Realizamos un número máximo de iteraciones
        vecinos = obtener_vecinos(estado_actual)  # Obtenemos los vecinos del estado actual
        mejor_vecino = None  # Inicializamos el mejor vecino
        mejor_heuristica = float('inf')  # Inicializamos la heurística del mejor vecino con un valor muy alto

        for vecino in vecinos:  # Iteramos sobre cada vecino
            if vecino not in tabu_list:  # Si el vecino no está en la lista Tabú
                heuristica = obtener_heuristica(vecino)  # Calculamos la heurística del vecino
                if heuristica < mejor_heuristica:  # Si el vecino tiene una mejor heurística (más baja)
                    mejor_heuristica = heuristica  # Actualizamos la heurística
                    mejor_vecino = vecino  # Guardamos este vecino como el mejor

        if mejor_vecino is None:  # Si no encontramos un vecino que mejore
            return estado_actual  # Terminamos y retornamos el estado actual como solución

        tabu_list.add(mejor_vecino)  # Añadimos el mejor vecino a la lista Tabú para evitar visitarlo nuevamente
        estado_actual = mejor_vecino  # Actualizamos el estado actual al mejor vecino encontrado

    return estado_actual  # Retornamos el estado encontrado después de las iteraciones
