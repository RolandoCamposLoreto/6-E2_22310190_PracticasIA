universo = ['Pedro', 'Ana', 'Luis']
es_estudiante = {
    'Pedro': True,
    'Ana': True,
    'Luis': False
}

def cuantificador_todo():
    try:
        for x in universo:
            if not es_estudiante.get(x, False):
                return False
        return True
    except Exception as e:
        print(f"Error al evaluar ∀x: {e}")
        return False

print("¿Todos son estudiantes? (∀x Estudiante(x)):", cuantificador_todo())
