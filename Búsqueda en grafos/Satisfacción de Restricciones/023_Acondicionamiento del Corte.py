import random
def acondicionamiento_del_corte(csp, max_iteraciones):
    """Limita la exploración de soluciones mediante un corte en la profundidad."""
    iteraciones = 0
    estado_actual = {}
    
    while iteraciones < max_iteraciones:
        # Realiza la búsqueda con un corte en la profundidad
        if csp.es_objetivo(estado_actual):
            return estado_actual
        # Realiza las asignaciones y verifica las restricciones
        for variable in csp.variables:
            if variable not in estado_actual:
                estado_actual[variable] = random.choice(csp.dominios[variable])
        iteraciones += 1
    
    return None  # Si alcanza el número máximo de iteraciones, retorna None
