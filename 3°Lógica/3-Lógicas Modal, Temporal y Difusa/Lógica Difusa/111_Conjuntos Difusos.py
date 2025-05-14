# -------------------------------
# Conjuntos Difusos: Función de pertenencia
# -------------------------------

# Función que define el grado de pertenencia de una temperatura al conjunto difuso "templado"
def pertenencia_temperatura(t):
    # Si la temperatura es menor o igual a 15°C, no pertenece al conjunto "templado"
    if t <= 15:
        return 0
    # Si la temperatura está entre 15°C y 25°C, la pertenencia crece linealmente de 0 a 1
    elif 15 < t <= 25:
        return (t - 15) / 10
    # Si la temperatura está entre 25°C y 35°C, la pertenencia decrece linealmente de 1 a 0
    elif 25 < t <= 35:
        return (35 - t) / 10
    # Si la temperatura es mayor a 35°C, no pertenece al conjunto "templado"
    else:
        return 0

# -------------------------------
# Evaluación de ejemplo
# -------------------------------

# Temperatura actual que queremos evaluar
temperatura = 22

# Llamada a la función con la temperatura dada y muestra del resultado
print(f"Grado de pertenencia de {temperatura}°C a 'templado':", pertenencia_temperatura(temperatura))
