# Base de conocimiento (hechos y reglas)
base_conocimiento = {
    'A': True,
    'B': False,
    'C': True,
}

# Regla de inferencia: Si A es verdadero, entonces B es verdadero
def regla():
    if base_conocimiento['A']:
        base_conocimiento['B'] = True
        print("B es ahora verdadero debido a A")

# Mostrar la base de conocimiento antes y después de aplicar la regla
print("Base de Conocimiento Antes:", base_conocimiento)
regla()
print("Base de Conocimiento Después:", base_conocimiento)
