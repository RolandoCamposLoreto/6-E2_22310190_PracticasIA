# Definimos la taxonomía de vehículos, donde "Vehículo" es la categoría general y
# tiene subcategorías como "Coche" y "Camión". "Coche" a su vez tiene subcategorías
# como "Sedán" y "SUV".

categorias = {
    "Vehículo": ["Coche", "Camión"],  # "Vehículo" tiene subcategorías "Coche" y "Camión"
    "Coche": ["Sedán", "SUV"]         # "Coche" tiene subcategorías "Sedán" y "SUV"
}

# Función que muestra las subcategorías de una categoría dada
def mostrar_taxonomia(clase):
    # Si la clase existe en la taxonomía, mostramos sus subcategorías
    if clase in categorias:
        print(f"{clase} tiene como subcategorías: {categorias[clase]}")
    else:
        # Si no tiene subcategorías, se indica que es una categoría final
        print(f"{clase} es una categoría final")

# Prueba con la clase "Vehículo"
mostrar_taxonomia("Vehículo")  # Debería mostrar: Vehículo tiene como subcategorías: ['Coche', 'Camión']
