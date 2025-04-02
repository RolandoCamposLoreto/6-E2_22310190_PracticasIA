def forward_checking(csp, estado, variable, valor):
    """Realiza la comprobación hacia adelante, eliminando valores inválidos en los dominios."""
    csp.dominios[variable] = [valor]  # Asigna el valor a la variable
    for vecino in csp.obtener_vecinos(variable):  # Revisa las variables relacionadas
        if valor in csp.dominios[vecino]:
            csp.dominios[vecino].remove(valor)  # Elimina valores inválidos
