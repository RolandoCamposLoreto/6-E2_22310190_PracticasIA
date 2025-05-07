base_prolog = {
    'padre': [('juan', 'ana'), ('juan', 'luis')],
    'madre': [('maria', 'ana')]
}

def es_padre(padre, hijo):
    return (padre, hijo) in base_prolog['padre']

def es_madre(madre, hijo):
    return (madre, hijo) in base_prolog['madre']

print("¿Juan es padre de Ana?", es_padre('juan', 'ana'))
print("¿María es madre de Luis?", es_madre('maria', 'luis'))
