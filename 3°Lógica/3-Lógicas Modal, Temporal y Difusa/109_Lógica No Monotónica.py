# Lógica no monotónica
# En esta lógica, la conclusión puede cambiar cuando se agrega nueva información.
# Ejemplo: una "ave" normalmente "vuela", pero si sabemos que es un "pingüino", ya no vuela.

# Diccionario de hechos conocidos
hechos = {
    "ave": True,      # Sabemos que es un ave
    "vuela": True     # Inicialmente inferimos que vuela
}

# Función de inferencia no monotónica
# Evalúa si el hecho "vuela" sigue siendo válido al introducir nueva información
def inferir():
    # Si es un ave y no se ha indicado que es un pingüino, se infiere que vuela
    if hechos.get("ave") and not hechos.get("pinguino"):
        hechos["vuela"] = True
    else:
        # Si se introduce el hecho de que es un pingüino, se revoca la inferencia anterior
        hechos["vuela"] = False

# Inferencia con información inicial
inferir()
print("¿Vuela?:", hechos["vuela"])  # Debería decir True

# Introducción de un nuevo hecho: ahora sabemos que es un pingüino
hechos["pinguino"] = True

# Nueva inferencia con el conocimiento actualizado
inferir()
print("¿Vuela después de saber que es pingüino?:", hechos["vuela"])  # Debería decir False
