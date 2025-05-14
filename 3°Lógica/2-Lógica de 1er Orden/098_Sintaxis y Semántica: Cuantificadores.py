# Definimos el universo de personas
universo = ['Pedro', 'Ana', 'Luis']

# Creamos un diccionario que nos indica si cada persona es estudiante o no
es_estudiante = {
    'Pedro': True,  # Pedro es estudiante
    'Ana': True,    # Ana es estudiante
    'Luis': False   # Luis no es estudiante
}

# Función para evaluar el cuantificador universal (∀x Estudiante(x))
def cuantificador_todo():
    try:
        # Iteramos sobre cada persona del universo
        for x in universo:
            # Si encontramos a alguien que no es estudiante, devolvemos False
            # Esto representa la negación de "todos son estudiantes"
            if not es_estudiante.get(x, False):
                return False
        # Si todos son estudiantes, devolvemos True
        return True
    except Exception as e:
        print(f"Error al evaluar ∀x: {e}")
        return False

# Evaluamos el cuantificador universal y mostramos el resultado
print("¿Todos son estudiantes? (∀x Estudiante(x)):", cuantificador_todo())
