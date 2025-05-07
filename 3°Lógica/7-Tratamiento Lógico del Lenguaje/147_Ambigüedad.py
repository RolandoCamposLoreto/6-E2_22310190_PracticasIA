# Verificación simple de ambigüedad en una expresión
def es_ambiguo(expresion):
    """
    Detecta la ambigüedad en una expresión basada en una gramática simple.
    """
    if "(" in expresion and ")" in expresion:
        return "Expresión ambigua."
    else:
        return "Expresión no ambigua."

# Ejemplo de expresión
expresion = "(x + y)"
resultado = es_ambiguo(expresion)
print(resultado)  # Salida: Expresión ambigua.
