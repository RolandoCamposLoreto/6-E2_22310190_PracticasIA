def propagacion_restricciones(csp, estado):
    """Propaga las restricciones a través del CSP, reduciendo dominios."""
    cambios = True
    while cambios:
        cambios = False
        for variable in csp.variables:
            if variable not in estado:
                for valor in csp.dominios[variable]:
                    if not csp.es_valido(estado, variable, valor):
                        csp.dominios[variable].remove(valor)  # Elimina valores inválidos
                        cambios = True  # Si hubo un cambio, se continúa propagando
