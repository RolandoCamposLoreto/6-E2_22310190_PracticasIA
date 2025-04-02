import random

def algoritmo_genetico(estado_inicial, obtener_heuristica, obtener_vecinos, poblacion_size=100, generaciones=100):
    # Inicializamos la población con el estado inicial
    poblacion = [estado_inicial] * poblacion_size  
    
    # Realizamos un número de generaciones
    for _ in range(generaciones):
        # Ordenamos la población en función de la heurística, de menor a mayor
        poblacion = sorted(poblacion, key=obtener_heuristica)
        
        nueva_poblacion = []  # Nueva población generada en esta iteración
        
        # Generamos nuevos individuos hasta llenar la nueva población
        while len(nueva_poblacion) < poblacion_size:
            # Seleccionamos a dos padres aleatorios de la mitad superior de la población
            padre = random.choice(poblacion[:poblacion_size // 2])
            madre = random.choice(poblacion[:poblacion_size // 2])
            
            # Generamos un hijo a partir de los vecinos del padre (esto debe ser reemplazado con un cruce y mutación)
            hijo = obtener_vecinos(padre)[0]  # Reemplazar con cruce y mutación adecuados
            nueva_poblacion.append(hijo)
        
        # La nueva población se convierte en la población para la siguiente generación
        poblacion = nueva_poblacion
        
    return poblacion[0]  # Retornamos el mejor estado de la población final
