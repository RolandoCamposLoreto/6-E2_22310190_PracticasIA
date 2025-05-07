# Lógica por defecto

base_conocimiento = {"ave": True}
por_defecto = {"vuela": True}

def evaluar():
    if base_conocimiento.get("pinguino"):
        return False
    return por_defecto["vuela"]

print("¿Vuelo por defecto?:", evaluar())
base_conocimiento["pinguino"] = True
print("¿Vuelo tras conocer que es pingüino?:", evaluar())
