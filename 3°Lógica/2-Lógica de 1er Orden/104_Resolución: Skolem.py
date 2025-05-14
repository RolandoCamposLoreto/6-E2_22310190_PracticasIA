# Función para skolemizar una fórmula lógica
def skolemizar(formula):
    try:
        # Verifica si la fórmula contiene el cuantificador existencial ∃
        if '∃' in formula:
            # Sustituye el cuantificador existencial ∃x por Skolem(x), representando la skolemización
            return formula.replace('∃x', 'Skolem(x)')
        return formula  # Si no contiene ∃, la fórmula se devuelve sin cambios
    except Exception as e:
        # En caso de error, se imprime el mensaje de error
        print("Error al skolemizar:", e)
        return formula  # Se devuelve la fórmula sin cambios en caso de error

# Prueba de la skolemización con la fórmula "∀y ∃x Ama(x, y)"
print("Fórmula skolemizada:", skolemizar("∀y ∃x Ama(x, y)"))
