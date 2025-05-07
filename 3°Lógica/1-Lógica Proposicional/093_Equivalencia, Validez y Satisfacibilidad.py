# Base de conocimiento
base_conocimiento = {
    'A': True,
    'B': True,
    'C': False,
}

def es_valido():
    try:
        # Asegurar que las variables existan
        if base_conocimiento.get('A') is not None and base_conocimiento.get('B') is not None:
            if base_conocimiento['A'] and base_conocimiento['B']:
                return True
            else:
                return False
        else:
            raise ValueError("Faltan variables en la base de conocimiento")
    except ValueError as e:
        print(f"Error en la validación: {e}")
        return False

# Verificación de validez
print("La proposición es válida:", es_valido())
