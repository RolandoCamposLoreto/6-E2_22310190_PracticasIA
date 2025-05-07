# Base de conocimiento
base_conocimiento = {
    'A': True,
    'B': True,
    'C': False,
}

def cnf():
    try:
        # Comprobar las condiciones antes de operar
        if base_conocimiento.get('A') is not None and base_conocimiento.get('B') is not None:
            if (base_conocimiento['A'] or base_conocimiento['B']) and (not base_conocimiento['A'] or base_conocimiento['B']):
                return True
            else:
                return False
        else:
            raise ValueError("Faltan variables en la base de conocimiento")
    except ValueError as e:
        print(f"Error en la resolución CNF: {e}")
        return False

# Verificación de la proposición en CNF
print("La proposición es verdadera en CNF:", cnf())
