# Diccionario "creencias" que contiene las creencias de diferentes personas sobre si llueve
# y si llevan o no paraguas. Cada clave es el nombre de una persona y su valor es otro diccionario
# con las creencias relacionadas con las condiciones climáticas y si llevan paraguas.
creencias = {
    "Ana": {"llueve": True, "lleva_paraguas": True},  # Ana cree que llueve y lleva paraguas
    "Luis": {"llueve": False, "lleva_paraguas": False}  # Luis cree que no llueve y no lleva paraguas
}

# Función que muestra las creencias de una persona dada como parámetro
def mostrar_creencias(persona):
    # Verificamos si la persona existe en el diccionario "creencias"
    if persona in creencias:
        # Si la persona está registrada, mostramos sus creencias
        print(f"Creencias de {persona}: {creencias[persona]}")
    else:
        # Si la persona no está registrada, mostramos un mensaje
        print("Persona no registrada")

# Llamamos a la función para mostrar las creencias de Ana
mostrar_creencias("Ana")
