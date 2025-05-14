def gramatica_causal(definicion):
    """
    Analiza una regla causal definida.
    Una regla causal tiene la forma "causa -> efecto", y esta función analiza la definición
    y devuelve una interpretación de la causa y el efecto asociados.
    """
    # Verificamos si la definición contiene "->", que indica la relación causal.
    if "->" in definicion:
        # Separamos la cadena en dos partes: la causa y el efecto
        causa, efecto = definicion.split("->")
        
        # Retornamos un mensaje interpretando la relación causal
        return f"La causa '{causa}' produce el efecto '{efecto}'."
    else:
        # Si la cadena no tiene la forma esperada, se muestra un error
        return "Error: definición causal inválida."

# Ejemplo de definición causal válida
definicion_causal = "Fuego -> Calor"
resultado = gramatica_causal(definicion_causal)
print(resultado)  # Salida: La causa 'Fuego' produce el efecto 'Calor'.

# Ejemplo de definición causal inválida
definicion_causal_invalida = "Fuego Calor"
resultado_invalido = gramatica_causal(definicion_causal_invalida)
print(resultado_invalido)  # Salida: Error: definición causal inválida.
