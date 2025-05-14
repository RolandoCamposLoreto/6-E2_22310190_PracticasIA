import random  # Importa el módulo random para generar números aleatorios. Es útil en este caso para asignar valores aleatorios a las variables y seleccionar variables en conflicto aleatoriamente.

def minimos_conflictos(csp, max_iteraciones=100):
    # Algoritmo de búsqueda local para resolver un problema CSP mediante la minimización de conflictos.
    # El algoritmo trata de encontrar una solución buscando variables con conflictos y asignando valores
    # que reduzcan la cantidad de conflictos en cada iteración.
    
    estado_actual = {var: random.choice(csp.dominios[var]) for var in csp.variables}  # Inicializa el estado actual asignando un valor aleatorio de su dominio a cada variable.
    
    for _ in range(max_iteraciones):  # Realiza un número máximo de iteraciones especificado por max_iteraciones.
        conflictos = []  # Lista para almacenar las variables que tienen conflictos
        
        for variable in csp.variables:  # Revisa todas las variables para identificar si su asignación actual causa un conflicto.
            if not csp.es_valido(estado_actual, variable, estado_actual[variable]):
                conflictos.append(variable)  # Si hay conflicto, se agrega la variable a la lista de conflictos
        
        if not conflictos:  # Si no hay conflictos, significa que hemos encontrado una solución válida.
            return estado_actual  # Si no hay conflictos, retorna el estado actual como solución
        
        variable_a_modificar = random.choice(conflictos)  # Escoge una variable con conflicto aleatoriamente.
        
        # Encuentra el valor que minimiza los conflictos dentro del dominio de la variable seleccionada.
        nuevo_valor = min(csp.dominios[variable_a_modificar], key=lambda val: csp.es_valido(estado_actual, variable_a_modificar, val))
        
        # Asigna el nuevo valor que minimiza los conflictos a la variable seleccionada.
        estado_actual[variable_a_modificar] = nuevo_valor  # Actualiza el estado actual con el nuevo valor
