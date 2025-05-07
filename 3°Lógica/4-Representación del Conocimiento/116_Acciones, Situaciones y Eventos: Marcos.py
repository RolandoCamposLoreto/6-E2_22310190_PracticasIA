marco_evento = {
    "evento": "Cena",
    "lugar": "Restaurante",
    "hora": "8 PM",
    "participantes": ["Ana", "Luis"]
}

def describir_evento(marco):
    for k, v in marco.items():
        print(f"{k}: {v}")

describir_evento(marco_evento)
