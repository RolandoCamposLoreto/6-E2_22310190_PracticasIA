# Base de conocimiento inicial con valores asignados a A, B, y C
base = {
    'A': True,
    'B': False,
    'C': False
}

# Función de encadenamiento hacia adelante
def encadenamiento_adelante():
    try:
        # Verifica si A es verdadero y C es falso
        # Si es cierto, entonces infiere que C es verdadero
        if base.get('A') and not base.get('C'):
            base['C'] = True
            print("Encadenamiento hacia adelante: inferido C")
        else:
            print("No es posible inferir C usando encadenamiento hacia adelante.")
    
    except Exception as e:
        # Captura cualquier excepción que pueda ocurrir en el proceso
        print(f"Error en el encadenamiento hacia adelante: {e}")

# Función de encadenamiento hacia atrás (un enfoque más dirigido a metas)
def encadenamiento_atras(meta):
    try:
        # Verifica si la meta es 'C'
        if meta == 'C':
            # Si la meta es C y A es verdadero, entonces infiere que C es verdadero
            if base.get('A'):
                base['C'] = True
                print("Encadenamiento hacia atrás: C inferido porque A es verdadero")
            else:
                print("No se puede inferir C usando encadenamiento hacia atrás, ya que A no es verdadero.")
        else:
            print("Meta no encontrada para encadenamiento hacia atrás.")
    
    except Exception as e:
        # Captura cualquier excepción que pueda ocurrir en el proceso
        print(f"Error en el encadenamiento hacia atrás: {e}")

# Ejecución de ambos tipos de encadenamiento
encadenamiento_adelante()  # Intenta inferir C de manera automática
encadenamiento_atras('C')  # Intenta inferir C basado en la meta

# Muestra el estado final de la base de conocimiento
print("Base de conocimiento después de encadenamiento:", base)
