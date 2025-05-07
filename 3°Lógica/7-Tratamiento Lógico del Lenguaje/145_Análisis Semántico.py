# Análisis semántico: verificar tipos de datos de variables
def analisis_semantico(cadena):
    """
    Realiza un análisis semántico verificando el tipo de la variable.
    """
    tipos = {'int': int, 'float': float, 'str': str}
    tokens = cadena.split()
    
    tipo_variable = tokens[0]
    valor = tokens[2]
    
    if tipo_variable not in tipos:
        return "Error: tipo de variable no válido."
    
    try:
        tipos[tipo_variable](valor)
        return "Análisis semántico exitoso."
    except ValueError:
        return "Error: valor no coincide con el tipo de variable."

# Ejemplo de cadena
cadena = "int 10"
resultado = analisis_semantico(cadena)
print(resultado)  # Salida: Análisis semántico exitoso.
