def conflicto_dirigido(csp, estado):
    """Detecta el conflicto y realiza un retroceso en el árbol de búsqueda."""
    for variable in csp.variables:
        if variable not in estado:  # Si la variable no está asignada
            for valor in csp.dominios[variable]:
                if not csp.es_valido(estado, variable, valor):
                    continue  # Si el valor causa conflicto, se prueba el siguiente
            return estado  # Si no se puede asignar un valor, retrocede
