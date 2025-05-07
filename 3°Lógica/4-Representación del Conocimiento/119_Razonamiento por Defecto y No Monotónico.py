hechos = {
    "ave": True,
    "vuela": True  # valor por defecto
}

def razonamiento_no_monotonico(hechos):
    if hechos.get("avestruz"):
        hechos["vuela"] = False
    return hechos["vuela"]

# Agregamos avestruz, y se modifica la conclusión
hechos["avestruz"] = True
print("¿El animal vuela?", razonamiento_no_monotonico(hechos))
