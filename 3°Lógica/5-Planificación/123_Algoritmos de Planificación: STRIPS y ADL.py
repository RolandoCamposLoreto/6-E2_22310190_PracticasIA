# Representación simple de STRIPS
estado_inicial = {"en_mesa": False, "objeto_en_silla": False}
acciones = [
    {"nombre": "colocar_en_mesa", "precondiciones": {"en_mesa": False}, "efectos": {"en_mesa": True}},
    {"nombre": "colocar_en_silla", "precondiciones": {"objeto_en_silla": False}, "efectos": {"objeto_en_silla": True}},
]

def aplicar_accion(estado, accion):
    if all(estado.get(k, False) == v for k, v in accion["precondiciones"].items()):
        estado.update(accion["efectos"])
        print(f"Acción '{accion['nombre']}' aplicada.")
        return True
    return False

# Ejecución de acciones
for accion in acciones:
    if aplicar_accion(estado_inicial, accion):
        print("Nuevo estado:", estado_inicial)
    else:
        print(f"Acción {accion['nombre']} no se puede aplicar.")
