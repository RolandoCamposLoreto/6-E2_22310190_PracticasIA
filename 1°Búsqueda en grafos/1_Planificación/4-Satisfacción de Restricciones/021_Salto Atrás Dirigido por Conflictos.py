# Función que detecta conflictos durante la asignación de valores en un problema CSP
# y realiza un retroceso si no se puede asignar un valor válido a alguna variable.
def conflicto_dirigido(csp, estado):
    """Detecta el conflicto y realiza un retroceso en el árbol de búsqueda."""
    
    # Recorre todas las variables del CSP.
    for variable in csp.variables:
        if variable not in estado:  # Si la variable no ha sido asignada aún
            # Recorre todos los valores posibles en el dominio de la variable.
            for valor in csp.dominios[variable]:
                # Verifica si la asignación de este valor es válida según las restricciones.
                if not csp.es_valido(estado, variable, valor):
                    continue  # Si el valor causa conflicto, se prueba el siguiente valor en el dominio
            # Si no se puede asignar un valor válido, realiza un retroceso (backtrack).
            return estado  # Si no se puede asignar un valor, retrocede (se regresa al estado anterior)
