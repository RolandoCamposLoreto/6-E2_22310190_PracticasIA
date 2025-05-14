# Define la función del algoritmo de búsqueda por haz local (local beam search),
# el cual mantiene k trayectorias (estados) simultáneamente y las actualiza en cada iteración
# con los mejores vecinos, buscando converger al mejor estado posible sin quedarse atrapado en óptimos locales.
def busqueda_haz_local(estado_inicial, obtener_heuristica, obtener_vecinos, k=5, max_iteraciones=100):
    frontera = [estado_inicial]  # Inicializamos la frontera con el estado inicial
    
    # Realizamos un número máximo de iteraciones
    for _ in range(max_iteraciones):
        nuevos_vecinos = []  # Lista para almacenar los nuevos vecinos generados
        
        # Generamos los vecinos de cada estado en la frontera
        for estado in frontera:
            nuevos_vecinos.extend(obtener_vecinos(estado))  # Añadimos los vecinos a la lista de nuevos vecinos
        
        # Seleccionamos los k vecinos con la mejor heurística
        frontera = sorted(nuevos_vecinos, key=obtener_heuristica)[:k]  # Ordenamos y seleccionamos los k mejores
        
    return frontera[0]  # Retornamos el mejor estado de la frontera
