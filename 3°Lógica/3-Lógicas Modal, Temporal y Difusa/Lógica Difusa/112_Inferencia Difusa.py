# Definimos la función de pertenencia difusa primero
def pertenencia_temperatura(t):
    if t <= 15:
        return 0
    elif 15 < t <= 25:
        return (t - 15) / 10
    elif 25 < t <= 35:
        return (35 - t) / 10
    else:
        return 0

# Luego usamos esa función en una inferencia difusa
def regla_difusa(temp):
    grado = pertenencia_temperatura(temp)
    if grado > 0.5:
        return "Ventilador al 60%"
    elif grado > 0:
        return "Ventilador al 30%"
    else:
        return "Ventilador apagado"

# Prueba
temp = 22
print(f"Inferencia difusa para {temp}°C:", regla_difusa(temp))
