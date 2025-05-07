acciones = {
    "esperar": 0.3,
    "salir_con_paraguas": 0.5,
    "salir_sin_paraguas": 0.2
}

def mejor_accion(probabilidades):
    return max(probabilidades, key=probabilidades.get)

print("La acción más racional es:", mejor_accion(acciones))
