# Función de propagación de restricciones que reduce los dominios de las variables
# en función de las restricciones del problema CSP.
def propagacion_restricciones(csp, estado):
    """Propaga las restricciones a través del CSP, reduciendo dominios."""
    
    cambios = True  # Inicializa una bandera para seguir propagando cambios
    while cambios:
        cambios = False  # Resetea la bandera en cada iteración del ciclo
        # Recorre todas las variables en el CSP.
        for variable in csp.variables:
            if variable not in estado:  # Si la variable no ha sido asignada aún
                # Recorre todos los posibles valores en el dominio de la variable.
                for valor in csp.dominios[variable]:
                    # Verifica si la asignación de un valor a la variable es válida.
                    if not csp.es_valido(estado, variable, valor):
                        csp.dominios[variable].remove(valor)  # Elimina el valor inválido
                        cambios = True  # Si hubo un cambio, continúa propagando restricciones
