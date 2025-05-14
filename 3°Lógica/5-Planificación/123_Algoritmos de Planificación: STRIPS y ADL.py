# Estado inicial del sistema: el objeto no está en la mesa ni en la silla
estado_inicial = {"en_mesa": False, "objeto_en_silla": False}

# Definición de las acciones disponibles
acciones = [
    {
        "nombre": "colocar_en_mesa",  # Nombre de la acción
        "precondiciones": {"en_mesa": False},  # La precondición es que el objeto no esté en la mesa
        "efectos": {"en_mesa": True}  # Efecto de la acción: el objeto pasa a estar en la mesa
    },
    {
        "nombre": "colocar_en_silla",  # Nombre de la acción
        "precondiciones": {"objeto_en_silla": False},  # La precondición es que el objeto no esté en la silla
        "efectos": {"objeto_en_silla": True}  # Efecto de la acción: el objeto pasa a estar en la silla
    }
]

# Función que aplica una acción al estado actual
def aplicar_accion(estado, accion):
    # Verificamos si todas las precondiciones de la acción se cumplen en el estado actual
    if all(estado.get(k, False) == v for k, v in accion["precondiciones"].items()):
        # Si las precondiciones son verdaderas, actualizamos el estado con los efectos de la acción
        estado.update(accion["efectos"])
        print(f"Acción '{accion['nombre']}' aplicada.")  # Mensaje indicando que la acción se aplicó
        return True  # La acción se aplicó correctamente
    return False  # Si las precondiciones no se cumplen, la acción no se puede aplicar

# Ejecución de las acciones
for accion in acciones:
    # Intentamos aplicar cada acción al estado actual
    if aplicar_accion(estado_inicial, accion):
        print("Nuevo estado:", estado_inicial)  # Si la acción se aplica, mostramos el nuevo estado
    else:
        print(f"Acción {accion['nombre']} no se puede aplicar.")  # Si no se puede aplicar, lo indicamos
