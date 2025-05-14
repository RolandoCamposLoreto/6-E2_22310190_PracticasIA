# Función que simula un sistema experto para diagnóstico basado en los síntomas proporcionados.
def sistema_experto(sintomas):
    # Verificamos si los síntomas incluyen 'fiebre' y 'tos'.
    if "fiebre" in sintomas and "tos" in sintomas:
        return "Posible gripe"  # Si ambos síntomas están presentes, el diagnóstico es "Posible gripe".
    
    # Si el síntoma 'dolor_cabeza' está presente, diagnosticamos "Posible migraña".
    elif "dolor_cabeza" in sintomas:
        return "Posible migraña"
    
    # Si ninguno de los casos anteriores se cumple, se considera que los síntomas son insuficientes.
    else:
        return "Síntomas insuficientes"

# Prueba de la función con los síntomas 'fiebre' y 'tos'.
print(sistema_experto(["fiebre", "tos"]))  # Esperamos que el sistema responda con "Posible gripe"
