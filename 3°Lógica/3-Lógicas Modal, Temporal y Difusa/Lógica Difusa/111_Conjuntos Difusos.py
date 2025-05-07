# Conjuntos difusos

def pertenencia_temperatura(t):
    if t <= 15:
        return 0
    elif 15 < t <= 25:
        return (t - 15) / 10
    elif 25 < t <= 35:
        return (35 - t) / 10
    else:
        return 0

temperatura = 22
print(f"Grado de pertenencia de {temperatura}°C a 'templado':", pertenencia_temperatura(temperatura))
