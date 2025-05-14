# Función de Forward Checking que realiza la comprobación hacia adelante en un problema CSP.
# La función asegura que los dominios de las variables relacionadas no contengan valores que violen las restricciones.
def forward_checking(csp, estado, variable, valor):
    """Realiza la comprobación hacia adelante, eliminando valores inválidos en los dominios."""
    
    # Asigna el valor a la variable en el dominio del CSP.
    csp.dominios[variable] = [valor]  # Asigna el valor a la variable

    # Revisa las variables relacionadas (vecinas) que están restringidas por la variable seleccionada.
    for vecino in csp.obtener_vecinos(variable):  # Revisa las variables relacionadas
        if valor in csp.dominios[vecino]:  # Si el valor está en el dominio de un vecino
            csp.dominios[vecino].remove(valor)  # Elimina el valor inválido del dominio del vecino
