ambiente = {'frente': 'pared', 'izquierda': 'libre'}

def agente_simple():
    try:
        if ambiente.get('frente') == 'pared':
            print("Agente: girar a la izquierda")
        elif ambiente.get('frente') == 'libre':
            print("Agente: avanzar")
        else:
            print("Agente: detenerse")
    except Exception as e:
        print("Error en comportamiento del agente:", e)

agente_simple()
