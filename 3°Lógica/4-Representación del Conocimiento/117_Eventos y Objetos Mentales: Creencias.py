creencias = {
    "Ana": {"llueve": True, "lleva_paraguas": True},
    "Luis": {"llueve": False, "lleva_paraguas": False}
}

def mostrar_creencias(persona):
    if persona in creencias:
        print(f"Creencias de {persona}: {creencias[persona]}")
    else:
        print("Persona no registrada")

mostrar_creencias("Ana")
