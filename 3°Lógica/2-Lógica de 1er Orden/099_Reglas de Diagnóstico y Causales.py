# Hechos que describen los síntomas de la persona
hechos = {
    'fiebre': True,        # La persona tiene fiebre
    'dolor_garganta': True, # La persona tiene dolor de garganta
    'infeccion': False     # Inicialmente, no se ha diagnosticado una infección
}

# Función para realizar un diagnóstico basado en los hechos
def diagnostico():
    try:
        # Verificar si la persona tiene fiebre y dolor de garganta
        if hechos.get('fiebre') and hechos.get('dolor_garganta'):
            # Si ambos síntomas están presentes, se diagnostica infección
            hechos['infeccion'] = True
            print("Diagnóstico: infección probable.")
        else:
            # Si no se cumplen las condiciones, no se puede determinar infección
            print("No se puede determinar infección.")
    except Exception as e:
        # Manejo de excepciones en caso de errores
        print("Error en el diagnóstico:", e)

# Llamada a la función de diagnóstico
diagnostico()

# Mostrar los hechos después de realizar el diagnóstico
print("Hechos después del diagnóstico:", hechos)
