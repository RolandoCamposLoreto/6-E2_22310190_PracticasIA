# Base de conocimiento: definimos un diccionario con las variables A, B y C
# A y B son valores booleanos, mientras que C es un valor booleano inicialmente falso.
base_conocimiento = {
    'A': True,  # Variable A está en True
    'B': True,  # Variable B está en True
    'C': False, # Variable C está en False (no se utiliza en la validación de este ejemplo)
}

def es_valido():
    try:
        # Verificamos si las variables A y B existen en la base de conocimiento
        # Usamos base_conocimiento.get() para evitar errores si alguna variable falta
        if base_conocimiento.get('A') is not None and base_conocimiento.get('B') is not None:
            # Si tanto A como B son verdaderos (True), la proposición es válida
            if base_conocimiento['A'] and base_conocimiento['B']:
                return True  # La proposición es válida
            else:
                return False  # La proposición no es válida porque A y/o B son falsos
        else:
            # Si falta alguna de las variables A o B, lanzamos un error indicando que la base de conocimiento está incompleta
            raise ValueError("Faltan variables en la base de conocimiento")
    except ValueError as e:
        # Capturamos cualquier error relacionado con la falta de variables en la base de conocimiento y lo imprimimos
        print(f"Error en la validación: {e}")
        return False  # Retornamos False si ocurrió un error en la validación

# Llamamos a la función es_valido() para verificar si la proposición es válida
# Esto imprimirá True si A y B son verdaderos, de lo contrario imprimirá False
print("La proposición es válida:", es_valido())  # Resultado esperado: True (porque A y B son ambos True)
