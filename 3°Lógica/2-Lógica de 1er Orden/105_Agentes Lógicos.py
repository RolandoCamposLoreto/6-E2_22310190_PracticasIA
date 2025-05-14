# Estado del ambiente (definiendo las condiciones del entorno)
ambiente = {'frente': 'pared', 'izquierda': 'libre'}

# Función que simula el comportamiento de un agente simple
def agente_simple():
    try:
        # Comprobamos si el frente del agente está bloqueado (hay una pared)
        if ambiente.get('frente') == 'pared':
            # Si hay una pared enfrente, el agente gira a la izquierda
            print("Agente: girar a la izquierda")
        # Comprobamos si el frente del agente está libre para avanzar
        elif ambiente.get('frente') == 'libre':
            # Si está libre, el agente puede avanzar
            print("Agente: avanzar")
        else:
            # Si ninguna de las condiciones anteriores se cumple, el agente se detiene
            print("Agente: detenerse")
    except Exception as e:
        # Si ocurre un error, se imprime el mensaje de error
        print("Error en comportamiento del agente:", e)

# Llamamos a la función para ejecutar el comportamiento del agente
agente_simple()
