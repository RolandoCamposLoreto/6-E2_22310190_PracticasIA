# Diccionario de hechos iniciales, donde el valor por defecto de "vuela" es True.
hechos = {
    "ave": True,
    "vuela": True  # Asumimos inicialmente que "vuela" es True
}

# Función que simula un razonamiento no monotónico
def razonamiento_no_monotonico(hechos):
    # Si el hecho "avestruz" es verdadero, modificamos la conclusión "vuela"
    if hechos.get("avestruz"):
        hechos["vuela"] = False  # El avestruz no vuela
    # Devolvemos la conclusión sobre si el animal vuela o no
    return hechos["vuela"]

# Agregamos el hecho de que el avestruz es un animal y modificamos la conclusión sobre "vuela"
hechos["avestruz"] = True
# Imprimimos el resultado de la función, que refleja el cambio en la conclusión
print("¿El animal vuela?", razonamiento_no_monotonico(hechos))
