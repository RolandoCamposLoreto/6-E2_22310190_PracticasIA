def backtracking(csp):
    def backtrack(estado):
        """Función recursiva de backtracking para resolver el CSP."""
        if csp.es_objetivo(estado):
            return estado  # Si se ha encontrado una solución completa, se devuelve el estado
        
        variable = next(var for var in csp.variables if var not in estado)  # Se elige la siguiente variable sin asignar
        
        # Probar los valores posibles de la variable
        for valor in csp.dominios[variable]:
            if csp.es_valido(estado, variable, valor):  # Verifica si la asignación es válida
                estado[variable] = valor  # Asigna el valor a la variable
                resultado = backtrack(estado)  # Llama recursivamente
                if resultado:  # Si encontró una solución, la devuelve
                    return resultado
                del estado[variable]  # Si no, retrocede (elimina la asignación)
        
        return None  # Si no hay solución, retorna None
    
    return backtrack({})  # Inicia el backtracking con el estado vacío
