import random

def minimos_conflictos(csp, max_iteraciones=100):
    """Algoritmo de búsqueda local para minimizar conflictos."""
    estado_actual = {var: random.choice(csp.dominios[var]) for var in csp.variables}
    
    for _ in range(max_iteraciones):
        conflictos = []
        for variable in csp.variables:
            if not csp.es_valido(estado_actual, variable, estado_actual[variable]):
                conflictos.append(variable)
        
        if not conflictos:
            return estado_actual  # Si no hay conflictos, se ha encontrado la solución
        
        variable_a_modificar = random.choice(conflictos)  # Escoge una variable en conflicto
        nuevo_valor = min(csp.dominios[variable_a_modificar], key=lambda val: csp.es_valido(estado_actual, variable_a_modificar, val))
        estado_actual[variable_a_modificar] = nuevo_valor  # Asigna el valor que minimiza los conflictos
