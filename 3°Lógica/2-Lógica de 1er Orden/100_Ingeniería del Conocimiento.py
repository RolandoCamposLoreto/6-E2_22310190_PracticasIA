# Diccionario que representa la base de conocimiento
base = {}

# Función para agregar un hecho a la base de conocimiento
def agregar_conocimiento(hecho, valor=True):
    try:
        # Verificar que el hecho no esté vacío
        if hecho:
            # Si el hecho es válido, se agrega a la base con el valor proporcionado
            base[hecho] = valor
            print(f"Agregado: {hecho} = {valor}")
        else:
            # Si el hecho es vacío o no válido, se muestra un mensaje de error
            print("Hecho no válido")
    except Exception as e:
        # Capturar y mostrar cualquier error que ocurra durante la ejecución
        print(f"Error al agregar el conocimiento: {e}")

# Llamadas a la función de agregar conocimiento
agregar_conocimiento("tiene_fiebre")  # Agrega 'tiene_fiebre' con valor por defecto True
agregar_conocimiento("tos", False)    # Agrega 'tos' con valor False

# Mostrar la base de conocimiento actualizada
print("Base de conocimiento actual:", base)
