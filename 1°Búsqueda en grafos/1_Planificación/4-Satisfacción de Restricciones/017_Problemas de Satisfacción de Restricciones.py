class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Variables que necesitan ser asignadas
        self.dominios = dominios  # Valores posibles para cada variable
        self.restricciones = restricciones  # Restricciones entre las variables
    
    def es_valido(self, estado, variable, valor):
        """Verifica si una asignación es válida según las restricciones del problema."""
        for (var, val) in estado.items():
            if (variable, var) in self.restricciones:
                if val == valor:
                    return False
        return True
    
    def es_objetivo(self, estado):
        """Verifica si se ha encontrado una solución válida (todas las variables asignadas)."""
        return len(estado) == len(self.variables)
    
    def obtener_vecinos(self, variable):
        """Devuelve las variables adyacentes de la variable en cuestión."""
        return [var for (var, _) in self.restricciones if var != variable]
