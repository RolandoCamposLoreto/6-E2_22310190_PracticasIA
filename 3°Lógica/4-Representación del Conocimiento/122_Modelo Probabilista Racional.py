# Definimos un diccionario con diferentes acciones y sus respectivas probabilidades de éxito.
acciones = {
    "esperar": 0.3,               # Probabilidad de éxito al esperar.
    "salir_con_paraguas": 0.5,    # Probabilidad de éxito al salir con paraguas.
    "salir_sin_paraguas": 0.2     # Probabilidad de éxito al salir sin paraguas.
}

# Función que determina cuál es la mejor acción en función de las probabilidades dadas.
def mejor_accion(probabilidades):
    # Usamos la función max para encontrar la acción con la mayor probabilidad.
    # 'key=probabilidades.get' le dice a la función max que compare los valores de probabilidad.
    return max(probabilidades, key=probabilidades.get)

# Llamamos a la función para encontrar la acción con la mayor probabilidad y la mostramos.
print("La acción más racional es:", mejor_accion(acciones))
