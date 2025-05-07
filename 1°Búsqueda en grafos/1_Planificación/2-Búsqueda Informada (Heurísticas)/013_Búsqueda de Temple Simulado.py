import random
import math

import random
import math

def busqueda_temple_simulado(estado_inicial, obtener_heuristica, obtener_vecinos, temperatura_inicial=1000, tasa_enfriamiento=0.995):
    estado_actual = estado_inicial  # Comenzamos con el estado inicial
    mejor_estado = estado_inicial  # El mejor estado encontrado inicialmente es el estado inicial
    mejor_heuristica = obtener_heuristica(estado_inicial)  # Calculamos la heurística del estado inicial
    temperatura = temperatura_inicial  # Inicializamos la temperatura al valor dado

    # Mientras la temperatura sea mayor que 1 (criterio de terminación)
    while temperatura > 1:
        vecinos = obtener_vecinos(estado_actual)  # Obtenemos los vecinos del estado actual
        vecino = random.choice(vecinos)  # Seleccionamos un vecino al azar
        delta_e = obtener_heuristica(vecino) - obtener_heuristica(estado_actual)  # Calculamos el cambio en la heurística
        
        # Si el vecino mejora la heurística o si se acepta la solución peor basado en la probabilidad
        if delta_e < 0 or random.random() < math.exp(-delta_e / temperatura):
            estado_actual = vecino  # Actualizamos el estado actual a este vecino
        
        # Si el nuevo estado es mejor que el mejor encontrado, lo guardamos
        if obtener_heuristica(estado_actual) < mejor_heuristica:
            mejor_heuristica = obtener_heuristica(estado_actual)  # Actualizamos la mejor heurística
            mejor_estado = estado_actual  # Actualizamos el mejor estado

        # Reducimos la temperatura según la tasa de enfriamiento
        temperatura *= tasa_enfriamiento

    return mejor_estado  # Retornamos el mejor estado encontrado después del enfriamiento
