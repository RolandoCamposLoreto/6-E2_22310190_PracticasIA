import re

def analisis_sintactico(cadena):
    """
    Realiza el análisis sintáctico usando una expresión regular para verificar la estructura.
    La estructura que estamos verificando es: una variable (identificador) seguida de un signo igual,
    un número entero y luego un punto y coma al final.
    """
    # Expresión regular que define la estructura esperada de la cadena:
    # - Empieza con una letra o guion bajo seguido de cualquier combinación de letras, números o guiones bajos (identificador).
    # - Luego, un espacio opcional, seguido del operador de asignación '='.
    # - Después, uno o más dígitos, y finalmente un punto y coma.
    patron = r'^[a-zA-Z_][a-zA-Z_0-9]*\s*=\s*\d+;$'
    
    # Usamos re.match para verificar si la cadena cumple con el patrón
    if re.match(patron, cadena):
        return "Cadena válida según la gramática."
    else:
        return "Cadena inválida según la gramática."

# Ejemplo de cadena
cadena = "x = 10;"
resultado = analisis_sintactico(cadena)
print(resultado)  # Salida: Cadena válida según la gramática.
