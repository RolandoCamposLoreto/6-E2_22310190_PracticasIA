ontologia = {
    "Animal": ["Mamífero", "Ave"],
    "Mamífero": ["Perro", "Gato"],
    "Ave": ["Pájaro", "Águila"]
}

def mostrar_ontologia(concepto):
    if concepto in ontologia:
        print(f"{concepto} incluye: {ontologia[concepto]}")
    else:
        print(f"{concepto} no tiene subcategorías")

mostrar_ontologia("Mamífero")
