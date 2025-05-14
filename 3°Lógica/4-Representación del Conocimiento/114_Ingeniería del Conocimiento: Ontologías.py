# Ontología: representación jerárquica de conceptos y subcategorías
# Aquí definimos una estructura tipo árbol donde cada concepto tiene sus subconceptos

ontologia = {
    "Animal": ["Mamífero", "Ave"],     # Un 'Animal' puede ser un 'Mamífero' o un 'Ave'
    "Mamífero": ["Perro", "Gato"],     # Un 'Mamífero' puede ser un 'Perro' o un 'Gato'
    "Ave": ["Pájaro", "Águila"]        # Un 'Ave' puede ser un 'Pájaro' o un 'Águila'
}

# Función que muestra las subcategorías de un concepto dado
def mostrar_ontologia(concepto):
    # Si el concepto existe en la ontología, se muestran sus subcategorías
    if concepto in ontologia:
        print(f"{concepto} incluye: {ontologia[concepto]}")
    else:
        # Si no hay subcategorías definidas, se informa
        print(f"{concepto} no tiene subcategorías")

# Prueba con un concepto existente
mostrar_ontologia("Mamífero")  # Debería mostrar: Mamífero incluye: ['Perro', 'Gato']
