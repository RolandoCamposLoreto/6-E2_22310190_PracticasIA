red_semantica = {
    "Perro": {"es_un": "Mamífero", "tiene": "Patas"},
    "Mamífero": {"es_un": "Animal"}
}

def describir_concepto(concepto):
    if concepto in red_semantica:
        for relacion, valor in red_semantica[concepto].items():
            print(f"{concepto} {relacion} {valor}")
    else:
        print("Concepto no encontrado")

describir_concepto("Perro")
