# Base de conocimiento
base_conocimiento = {
    'A': True,
    'B': False,
    'C': False,
}

def inferencia_logica():
    try:
        # Verificar la base de conocimiento
        if base_conocimiento.get('A') is not None and base_conocimiento.get('B') is not None:
            if base_conocimiento['A'] and base_conocimiento['B']:
                base_conocimiento['C'] = True
                print("Se ha inferido que C es verdadero")
            else:
                print("No se puede inferir C, ya que A y B no son ambos verdaderos.")
        else:
            raise ValueError("Faltan variables en la base de conocimiento")

    except ValueError as e:
        print(f"Error en la inferencia: {e}")

# Llamada a la función de inferencia
inferencia_logica()
print("Base de Conocimiento Después de la Inferencia:", base_conocimiento)
