import re

def analisis_lexico(cadena):
    """
    Realiza el análisis léxico dividiendo una cadena de texto en tokens.
    La función utiliza expresiones regulares para identificar los diferentes tipos de tokens
    como palabras (identificadores), números, operadores matemáticos y delimitadores.
    """
    # Expresiones regulares para detectar diferentes tipos de tokens
    patrones = {
        'palabra': r'\b[a-zA-Z_][a-zA-Z_0-9]*\b',  # Palabras (identificadores): Empieza con letra o guion bajo y luego puede contener letras, números o guiones bajos.
        'numero': r'\b\d+\b',  # Números enteros: Secuencia de dígitos.
        'operador': r'[+\-*/=]',  # Operadores matemáticos: +, -, *, /, =.
        'delimitador': r'[;,.]',  # Delimitadores: Punto y coma, coma, punto.
    }
    
    tokens = []  # Lista para almacenar los tokens encontrados.
    
    # Iterar sobre los patrones para encontrar las coincidencias en la cadena.
    for tipo, patron in patrones.items():
        # Buscar todas las coincidencias en la cadena usando la expresión regular correspondiente
        for coincidencia in re.finditer(patron, cadena):
            # Agregar el tipo de token y el valor del token encontrado a la lista de tokens
            tokens.append((tipo, coincidencia.group()))
    
    return tokens  # Retornar la lista de tokens encontrados.

# Ejemplo de cadena
cadena = "int x = 10; y = 20 + x;"
tokens = analisis_lexico(cadena)
print(tokens)  # Salida: [('palabra', 'int'), ('palabra', 'x'), ('operador', '='), ('numero', '10'), ('delimitador', ';'), ('palabra', 'y'), ('operador', '='), ('numero', '20'), ('operador', '+'), ('palabra', 'x'), ('delimitador', ';')]
