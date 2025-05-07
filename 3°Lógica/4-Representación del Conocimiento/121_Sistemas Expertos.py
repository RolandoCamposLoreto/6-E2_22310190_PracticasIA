def sistema_experto(sintomas):
    if "fiebre" in sintomas and "tos" in sintomas:
        return "Posible gripe"
    elif "dolor_cabeza" in sintomas:
        return "Posible migraña"
    else:
        return "Síntomas insuficientes"

# Prueba
print(sistema_experto(["fiebre", "tos"]))
