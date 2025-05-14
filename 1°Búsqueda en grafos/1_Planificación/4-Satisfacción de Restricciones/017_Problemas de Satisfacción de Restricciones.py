# Clase que implementa un problema de satisfacción de restricciones (CSP).
# Un CSP es un problema en el cual se deben asignar valores a un conjunto de variables de manera que se cumplan todas las restricciones definidas entre ellas.
class CSP:
    # Constructor que inicializa las variables, dominios y restricciones del problema CSP.
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables que necesitan ser asignadas en el problema CSP.
        self.dominios = dominios    # Diccionario que define los posibles valores para cada variable.
        self.restricciones = restricciones  # Lista de restricciones entre las variables (pares de variables relacionadas).

    # Verifica si una asignación de valor a una variable es válida según las restricciones del problema CSP.
    def es_valido(self, estado, variable, valor):
        # Recorre todas las asignaciones actuales en el estado.
        for (var, val) in estado.items():
            # Verifica si hay una restricción entre la variable actual y las ya asignadas.
            if (variable, var) in self.restricciones:
                # Si las variables tienen el mismo valor, la asignación es inválida.
                if val == valor:
                    return False
        # Si no se encuentra ninguna violación, la asignación es válida.
        return True

    # Verifica si el estado actual ha alcanzado una solución válida, es decir, todas las variables están asignadas.
    def es_objetivo(self, estado):
        # Compara la cantidad de asignaciones con el número total de variables.
        return len(estado) == len(self.variables)

    # Devuelve las variables adyacentes a la variable actual (variables que están restringidas por las restricciones).
    def obtener_vecinos(self, variable):
        # Filtra las variables adyacentes relacionadas con la variable actual según las restricciones.
        return [var for (var, _) in self.restricciones if var != variable]
