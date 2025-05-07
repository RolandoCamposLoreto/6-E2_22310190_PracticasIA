# Lógica no monotónica

hechos = {"ave": True, "vuela": True}

def inferir():
    if hechos.get("ave") and not hechos.get("pinguino"):
        hechos["vuela"] = True
    else:
        hechos["vuela"] = False

# Inicialmente
inferir()
print("¿Vuela?:", hechos["vuela"])

# Nueva información
hechos["pinguino"] = True
inferir()
print("¿Vuela después de saber que es pingüino?:", hechos["vuela"])
