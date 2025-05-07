base = {
    'A': True,
    'B': False,
    'C': False
}

def encadenamiento_adelante():
    if base.get('A') and not base.get('C'):
        base['C'] = True
        print("Encadenamiento hacia adelante: inferido C")

def encadenamiento_atras(meta):
    if meta == 'C':
        if base.get('A'):
            base['C'] = True
