def analisis_semantico(cadena):
    """
    Realiza un análisis semántico verificando el tipo de la variable.
    El análisis semántico valida si el valor de la variable es compatible con su tipo de datos.
    """
    # Definir los tipos de variables permitidos en el análisis (tipos básicos)
    # 'int': entero, 'float': número decimal, 'str': cadena de texto
    tipos = {'int': int, 'float': float, 'str': str}
    
    # La cadena se debe separar en tokens, considerando el formato 'tipo_variable valor'.
    # Utilizamos el método split() para separar la cadena en palabras.
    tokens = cadena.split()
    
    # Si la cadena no tiene exactamente dos elementos (tipo de variable y valor), se genera un error.
    if len(tokens) != 2:
        return "Error: la cadena debe tener la forma 'tipo_variable valor'."
    
    # Extraemos el tipo de la variable y su valor de los tokens
    tipo_variable = tokens[0]
    valor = tokens[1]
    
    # Verificamos si el tipo de variable es uno de los tipos válidos (definidos anteriormente)
    if tipo_variable not in tipos:
        return "Error: tipo de variable no válido."
    
    # Intentamos convertir el valor al tipo correspondiente según el tipo de la variable.
    # Esto nos ayuda a verificar si el valor coincide con el tipo especificado.
    try:
        tipos[tipo_variable](valor)  # Intentamos convertir el valor al tipo correspondiente
        return "Análisis semántico exitoso."  # Si no ocurre un error, el análisis es exitoso.
    except ValueError:
        # Si no se puede convertir el valor (por ejemplo, "10a" no se puede convertir a int),
        # se captura el error y se indica que el valor no coincide con el tipo.
        return "Error: valor no coincide con el tipo de variable."

# Ejemplo de cadena válida: el tipo de la variable es 'int' y el valor es '10'.
cadena = "int 10"
resultado = analisis_semantico(cadena)
print(resultado)  # Salida: Análisis semántico exitoso.

# Ejemplo con error: el valor '10a' no puede ser convertido a tipo 'float', por lo que se genera un error.
cadena = "float 10a"
resultado = analisis_semantico(cadena)
print(resultado)  # Salida: Error: valor no coincide con el tipo de variable.
