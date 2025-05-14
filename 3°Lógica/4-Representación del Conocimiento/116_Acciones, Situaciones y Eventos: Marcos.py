# Definimos un diccionario llamado "marco_evento" que contiene información sobre un evento:
# - El tipo de evento ("Cena").
# - El lugar del evento ("Restaurante").
# - La hora en que se lleva a cabo el evento ("8 PM").
# - Los participantes del evento ("Ana" y "Luis").

marco_evento = {
    "evento": "Cena",  # Tipo de evento
    "lugar": "Restaurante",  # Lugar del evento
    "hora": "8 PM",  # Hora en que ocurre el evento
    "participantes": ["Ana", "Luis"]  # Lista de participantes
}

# Función que describe un evento iterando sobre las claves y valores del diccionario "marco".
def describir_evento(marco):
    # Recorremos cada par clave-valor del diccionario
    for k, v in marco.items():
        # Imprimimos cada clave y su valor correspondiente
        print(f"{k}: {v}")

# Llamamos a la función para describir el evento utilizando el diccionario "marco_evento"
describir_evento(marco_evento)
