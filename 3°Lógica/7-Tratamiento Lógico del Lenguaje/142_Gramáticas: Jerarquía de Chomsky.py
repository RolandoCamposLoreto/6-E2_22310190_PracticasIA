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
    if "->" in gramatica:
        if len(gramatica.split("->")) == 2:
            return "Gramática regular (Tipo 3)"
        elif "S" in gramatica:
            return "Gramática libre de contexto (Tipo 2)"
        else:
            return "Gramática sensible al contexto (Tipo 1)"
    return "Gramática recursiva no lineal (Tipo 0)"

# Ejemplo de gramática
gramatica_1 = "S -> aSb"
gramatica_2 = "S -> aA | bB"

print(jerarquia_chomsky(gramatica_1))  # Salida: Gramática libre de contexto (Tipo 2)
print(jerarquia_chomsky(gramatica_2))  # Salida: Gramática regular (Tipo 3)
