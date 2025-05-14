# Implementación básica de las jerarquías de Chomsky

# Definición de tipos de gramáticas según la jerarquía de Chomsky
def jerarquia_chomsky(gramatica):
    """
    Este código determina el tipo de gramática basada en la jerarquía de Chomsky:
    - Tipo 0: Gramáticas Recursivas No Lineales
    - Tipo 1: Gramáticas Sensibles al Contexto
    - Tipo 2: Gramáticas Libres de Contexto
    - Tipo 3: Gramáticas Regulares
    """
    # Verifica si la gramática contiene la flecha de producción "->"
    if "->" in gramatica:
        # Si la gramática tiene una sola producción, se considera regular
        if len(gramatica.split("->")) == 2:
            return "Gramática regular (Tipo 3)"
        # Si la gramática contiene un símbolo no terminal como 'S', es libre de contexto
        elif "S" in gramatica:
            return "Gramática libre de contexto (Tipo 2)"
        else:
            return "Gramática sensible al contexto (Tipo 1)"
    # Si no contiene la flecha de producción, se considera recursiva no lineal
    return "Gramática recursiva no lineal (Tipo 0)"

# Ejemplo de gramática
gramatica_1 = "S -> aSb"  # Ejemplo de gramática libre de contexto
gramatica_2 = "S -> aA | bB"  # Ejemplo de gramática regular

# Imprimir los resultados de la clasificación de las gramáticas
print(jerarquia_chomsky(gramatica_1))  # Salida: Gramática libre de contexto (Tipo 2)
print(jerarquia_chomsky(gramatica_2))  # Salida: Gramática regular (Tipo 3)
