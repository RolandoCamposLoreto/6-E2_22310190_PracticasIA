# Lógica por defecto
# Este tipo de lógica permite asumir hechos por omisión, siempre que no haya información que los contradiga.
# Por ejemplo: "Las aves vuelan (por defecto), a menos que se sepa que es un pingüino".

# Base de conocimiento explícita (hechos que sabemos con certeza)
base_conocimiento = {
    "ave": True  # Sabemos que es un ave
}

# Supuesto por defecto: las aves vuelan, a menos que se indique lo contrario
por_defecto = {
    "vuela": True  # Asumimos que vuela mientras no se contradiga esta suposición
}

# Evaluación basada en la lógica por defecto
def evaluar():
    # Si se sabe que es un pingüino, se contradice el vuelo por defecto
    if base_conocimiento.get("pinguino"):
        return False  # Se anula el vuelo por defecto
    # Si no hay contradicción, se acepta la suposición de que vuela
    return por_defecto["vuela"]

# Primera evaluación: solo sabemos que es un ave, así que se asume que vuela
print("¿Vuelo por defecto?:", evaluar())  # Debería decir True

# Se introduce nueva información: también sabemos que es un pingüino
base_conocimiento["pinguino"] = True

# Segunda evaluación: la nueva información contradice el supuesto por defecto
print("¿Vuelo tras conocer que es pingüino?:", evaluar())  # Debería decir False
