# Análisis sintáctico: verificar si una cadena sigue una gramática específica
# Usando una gramática simple para demostración

import re

def analisis_sintactico(cadena):
    """
    Realiza el análisis sintáctico usando una expresión regular para verificar la estructura.
    """
    patron = r'^[a-zA-Z_][a-zA-Z_0-9]*\s*=\s*\d+;$'
    if re.match(patron, cadena):
        return "Cadena válida según la gramática."
    else:
        return "Cadena inválida según la gramática."

# Ejemplo de cadena
cadena = "x = 10;"
resultado = analisis_sintactico(cadena)
print(resultado)  # Salida: Cadena válida según la gramática.
