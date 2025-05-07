def skolemizar(formula):
    try:
        if '∃' in formula:
            return formula.replace('∃x', 'Skolem(x)')
        return formula
    except Exception as e:
        print("Error al skolemizar:", e)
        return formula

print("Fórmula skolemizada:", skolemizar("∀y ∃x Ama(x, y)"))
