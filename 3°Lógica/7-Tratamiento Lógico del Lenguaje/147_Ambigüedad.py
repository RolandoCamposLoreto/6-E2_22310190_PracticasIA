def es_ambiguo(expresion):
    """
    Detecta la ambigüedad en una expresión basada en una gramática simple.
    En este caso, considera que una expresión es ambigua si contiene paréntesis.
    """
    # Verificamos si la expresión contiene paréntesis abiertos '(' y cerrados ')'
    if "(" in expresion and ")" in expresion:
        return "Expresión ambigua."  # Si contiene paréntesis, es considerada ambigua
    else:
        return "Expresión no ambigua."  # Si no contiene paréntesis, no es ambigua

# Ejemplo de expresión con paréntesis
expresion = "(x + y)"
resultado = es_ambiguo(expresion)
print(resultado)  # Salida: Expresión ambigua.
