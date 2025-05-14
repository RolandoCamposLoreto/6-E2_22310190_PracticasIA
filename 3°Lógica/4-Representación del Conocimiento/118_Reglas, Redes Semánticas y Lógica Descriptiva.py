# Diccionario "red_semantica" que describe las relaciones semánticas entre conceptos.
# Cada clave es un concepto, y su valor es otro diccionario que especifica sus relaciones
# con otros conceptos (por ejemplo, "es_un" o "tiene").
red_semantica = {
    "Perro": {"es_un": "Mamífero", "tiene": "Patas"},  # El Perro es un Mamífero y tiene Patas
    "Mamífero": {"es_un": "Animal"}  # El Mamífero es un Animal
}

# Función que describe un concepto, mostrando sus relaciones con otros conceptos
def describir_concepto(concepto):
    # Verificamos si el concepto existe en la red semántica
    if concepto in red_semantica:
        # Si el concepto está presente, recorremos las relaciones de ese concepto
        for relacion, valor in red_semantica[concepto].items():
            # Imprimimos las relaciones con el formato: Concepto relación Valor
            print(f"{concepto} {relacion} {valor}")
    else:
        # Si el concepto no está en la red, mostramos un mensaje indicando que no se encontró
        print("Concepto no encontrado")

# Llamamos a la función para describir el concepto "Perro"
describir_concepto("Perro")
