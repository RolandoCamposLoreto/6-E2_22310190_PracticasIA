# Función principal de backtracking para resolver un problema CSP.
# Utiliza una estrategia recursiva para explorar las posibles asignaciones de valores a las variables del CSP.
def backtracking(csp):
    # Función recursiva que intenta asignar valores a las variables del CSP.
    def backtrack(estado):
        """Función recursiva de backtracking para resolver el CSP."""
        
        # Si el estado actual es una solución válida (todas las variables están asignadas), retorna el estado.
        if csp.es_objetivo(estado):
            return estado  # Si se ha encontrado una solución completa, se devuelve el estado
        
        # Selecciona la siguiente variable que no ha sido asignada en el estado.
        variable = next(var for var in csp.variables if var not in estado)  # Se elige la siguiente variable sin asignar
        
        # Probar los valores posibles de la variable seleccionada.
        for valor in csp.dominios[variable]:  # Itera sobre los valores posibles para la variable.
            # Verifica si la asignación de un valor a la variable es válida según las restricciones.
            if csp.es_valido(estado, variable, valor):  # Verifica si la asignación es válida
                estado[variable] = valor  # Asigna el valor a la variable en el estado actual
                resultado = backtrack(estado)  # Llama recursivamente a backtrack con el nuevo estado
                if resultado:  # Si se ha encontrado una solución válida en la llamada recursiva
                    return resultado  # Retorna la solución encontrada
                del estado[variable]  # Si no se encuentra solución, retrocede (elimina la asignación de la variable)
        
        # Si no se ha encontrado una solución válida después de probar todos los valores posibles, retorna None.
        return None  # Si no hay solución, retorna None
    
    return backtrack({})  # Inicia el backtracking con el estado vacío (sin asignaciones iniciales)
