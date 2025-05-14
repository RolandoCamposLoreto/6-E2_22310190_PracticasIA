# Diccionario con las reglas de certeza para cada síntoma.
# El valor de cada clave representa el factor de certeza asociado con ese síntoma.
reglas = {
    "tiene_fiebre": 0.8,  # El factor de certeza de tener fiebre es 0.8
    "dolor_garganta": 0.6  # El factor de certeza de tener dolor de garganta es 0.6
}

# Función que calcula el factor de certeza total para el diagnóstico.
def factor_de_certeza(reglas):
    certeza_total = 1  # Inicializamos la certeza total en 1 (100%)
    
    # Multiplicamos los factores de certeza de cada síntoma.
    for valor in reglas.values():
        certeza_total *= valor  # Multiplicamos el valor del factor de certeza por cada síntoma.
    
    return certeza_total  # Retornamos el factor total de certeza.

# Imprimimos el resultado, redondeado a dos decimales, para obtener el factor de certeza total.
print("Factor de certeza para diagnóstico:", round(factor_de_certeza(reglas), 2))
