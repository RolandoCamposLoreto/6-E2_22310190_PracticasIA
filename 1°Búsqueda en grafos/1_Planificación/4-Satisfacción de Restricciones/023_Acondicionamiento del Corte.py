import random  # Importa el módulo random para generar números aleatorios, utilizados para asignar valores aleatorios a las variables del CSP.

def acondicionamiento_del_corte(csp, max_iteraciones):
    """
    Limita la exploración de soluciones mediante un corte en la profundidad.
    Realiza una búsqueda con asignación aleatoria de valores a las variables hasta
    alcanzar un número máximo de iteraciones o encontrar una solución válida.
    """
    
    iteraciones = 0  # Inicializa el contador de iteraciones, para limitar la profundidad de la búsqueda
    estado_actual = {}  # Diccionario que almacenará el estado de las asignaciones de las variables
    
    # Ciclo principal de la búsqueda, que se ejecuta hasta alcanzar el número máximo de iteraciones.
    while iteraciones < max_iteraciones:
        if csp.es_objetivo(estado_actual):  # Si el estado actual es una solución válida
            return estado_actual  # Devuelve el estado actual si cumple con el objetivo
        
        # Asigna valores aleatorios a las variables que aún no tienen un valor asignado
        for variable in csp.variables:
            if variable not in estado_actual:  # Si la variable aún no tiene asignado un valor
                estado_actual[variable] = random.choice(csp.dominios[variable])  # Asigna un valor aleatorio desde su dominio
        
        iteraciones += 1  # Incrementa el contador de iteraciones
    
    return None  # Si no se alcanza el objetivo en el número máximo de iteraciones, retorna None
