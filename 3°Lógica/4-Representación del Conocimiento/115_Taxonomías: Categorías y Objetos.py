categorias = {
    "Vehículo": ["Coche", "Camión"],
    "Coche": ["Sedán", "SUV"]
}

def mostrar_taxonomia(clase):
    if clase in categorias:
        print(f"{clase} tiene como subcategorías: {categorias[clase]}")
    else:
        print(f"{clase} es una categoría final")

mostrar_taxonomia("Vehículo")
