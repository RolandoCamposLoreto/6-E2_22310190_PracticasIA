# Implementación de una gramática causal (simplificada)

def gramatica_causal(definicion):
    """
    Analiza una regla causal definida.
    """
    # Ejemplo de una regla causal de forma "causa -> efecto"
    if "->" in definicion:
        causa, efecto = definicion.split("->")
        return f"La causa '{causa}' produce el efecto '{efecto}'."
    else:
        return "Error: definición causal inválida."

# Ejemplo de definición causal
definicion_causal = "Fuego -> Calor"
resultado = gramatica_causal(definicion_causal)
print(resultado)  # Salida: La causa 'Fuego' produce el efecto 'Calor'.
