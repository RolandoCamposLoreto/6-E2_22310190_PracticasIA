hechos = {
    'fiebre': True,
    'dolor_garganta': True,
    'infeccion': False
}

def diagnostico():
    try:
        if hechos.get('fiebre') and hechos.get('dolor_garganta'):
            hechos['infeccion'] = True
            print("Diagnóstico: infección probable.")
        else:
            print("No se puede determinar infección.")
    except Exception as e:
        print("Error en el diagnóstico:", e)

diagnostico()
print("Hechos después del diagnóstico:", hechos)
