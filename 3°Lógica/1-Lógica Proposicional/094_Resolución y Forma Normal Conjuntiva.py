# Base de conocimiento: definimos un diccionario con las variables A, B y C
# A y B son valores booleanos, mientras que C es un valor booleano inicialmente falso.
base_conocimiento = {
    'A': True,  # Variable A está en True
    'B': True,  # Variable B está en True
    'C': False, # Variable C está en False (no se utiliza en este ejemplo)
}

def cnf():
    try:
        # Verificamos si las variables A y B existen en la base de conocimiento
        # Usamos base_conocimiento.get() para evitar errores si alguna variable falta
        if base_conocimiento.get('A') is not None and base_conocimiento.get('B') is not None:
            # Aquí estamos evaluando si la proposición está en Forma Normal Conjuntiva (CNF)
            # La CNF de una proposición es una conjunción de cláusulas disyuntivas.
            # Evaluamos dos cláusulas en forma disyuntiva: 
            # (A OR B) AND (NOT A OR B)
            if (base_conocimiento['A'] or base_conocimiento['B']) and (not base_conocimiento['A'] or base_conocimiento['B']):
                return True  # La proposición es válida en CNF
            else:
                return False  # La proposición no es válida en CNF
        else:
            # Si falta alguna de las variables A o B, lanzamos un error indicando que la base de conocimiento está incompleta
            raise ValueError("Faltan variables en la base de conocimiento")
    except ValueError as e:
        # Capturamos cualquier error relacionado con la falta de variables en la base de conocimiento y lo imprimimos
        print(f"Error en la resolución CNF: {e}")
        return False  # Retornamos False si ocurrió un error en la validación

# Llamamos a la función cnf() para verificar si la proposición es verdadera en CNF
# Esto imprimirá True si la proposición es válida en CNF, de lo contrario imprimirá False
print("La proposición es verdadera en CNF:", cnf())  # Resultado esperado: True (porque la proposición es válida en CNF)
