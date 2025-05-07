base = {}

def agregar_conocimiento(hecho, valor=True):
    if hecho:
        base[hecho] = valor
        print(f"Agregado: {hecho} = {valor}")
    else:
        print("Hecho no válido")

agregar_conocimiento("tiene_fiebre")
agregar_conocimiento("tos", False)
print("Base de conocimiento actual:", base)
