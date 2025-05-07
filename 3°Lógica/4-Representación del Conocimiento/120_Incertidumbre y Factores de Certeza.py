reglas = {
    "tiene_fiebre": 0.8,
    "dolor_garganta": 0.6
}

def factor_de_certeza(reglas):
    certeza_total = 1
    for valor in reglas.values():
        certeza_total *= valor
    return certeza_total

print("Factor de certeza para diagnóstico:", round(factor_de_certeza(reglas), 2))
