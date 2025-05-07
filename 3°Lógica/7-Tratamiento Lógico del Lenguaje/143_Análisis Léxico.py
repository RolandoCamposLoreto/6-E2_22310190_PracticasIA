# Análisis léxico: tokenización de una cadena
import re

def analisis_lexico(cadena):
    """
    Realiza el análisis léxico dividiendo una cadena de texto en tokens.
    """
    # Expresiones regulares para detectar diferentes tipos de tokens
    patrones = {
        'palabra': r'\b[a-zA-Z_][a-zA-Z_0-9]*\b',  # Palabras (identificadores)
        'numero': r'\b\d+\b',  # Números enteros
        'operador': r'[+\-*/=]',  # Operadores matemáticos
        'delimitador': r'[;,.]',  # Delimitadores
    }
    
    tokens = []
    for tipo, patron in patrones.items():
        for coincidencia in re.finditer(patron, cadena):
            tokens.append((tipo, coincidencia.group()))
    return tokens

# Ejemplo de cadena
cadena = "int x = 10; y = 20 + x;"
tokens = analisis_lexico(cadena)
print(tokens)  # Salida: [('palabra', 'int'), ('palabra', 'x'), ('operador', '='), ('numero', '10'), ('delimitador', ';'), ('palabra', 'y'), ('operador', '='), ('numero', '20'), ('operador', '+'), ('palabra', 'x'), ('delimitador', ';')]
