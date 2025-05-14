# -----------------------------------------------
# Función de pertenencia difusa: conjunto "templado"
# -----------------------------------------------
def pertenencia_temperatura(t):
    # Si la temperatura es menor o igual a 15°C, la pertenencia es 0 (muy frío)
    if t <= 15:
        return 0
    # Si la temperatura está entre 15°C y 25°C, la pertenencia aumenta linealmente de 0 a 1
    elif 15 < t <= 25:
        return (t - 15) / 10
    # Si la temperatura está entre 25°C y 35°C, la pertenencia disminuye linealmente de 1 a 0
    elif 25 < t <= 35:
        return (35 - t) / 10
    # Si la temperatura es mayor a 35°C, la pertenencia vuelve a 0 (muy caliente)
    else:
        return 0

# -----------------------------------------------
# Inferencia difusa basada en el grado de pertenencia
# -----------------------------------------------
def regla_difusa(temp):
    # Obtenemos el grado de pertenencia de la temperatura al conjunto "templado"
    grado = pertenencia_temperatura(temp)

    # Inferencia difusa basada en reglas simples:
    if grado > 0.5:
        return "Ventilador al 60%"  # Temperatura moderadamente alta → ventilación media-alta
    elif grado > 0:
        return "Ventilador al 30%"  # Temperatura algo templada → ventilación baja
    else:
        return "Ventilador apagado"  # Temperatura muy baja o muy alta fuera del rango de "templado"

# -----------------------------------------------
# Prueba del sistema difuso con una temperatura específica
# -----------------------------------------------
temp = 22
print(f"Inferencia difusa para {temp}°C:", regla_difusa(temp))
