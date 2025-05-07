import random

# Definir los estados de Markov y las probabilidades de transición
estados = ['A', 'B']
transiciones = {
    'A': {'A': 0.7, 'B': 0.3},
    'B': {'A': 0.4, 'B': 0.6}
}

# Función para simular un proceso de Markov
def proceso_markov(inicio, pasos):
    estado_actual = inicio
    secuencia = [estado_actual]
    for _ in range(pasos):
        estado_actual = random.choices(estados, weights=[transiciones[estado_actual]['A'], transiciones[estado_actual]['B']])[0]
        secuencia.append(estado_actual)
    return secuencia

# Simulación del proceso de Markov
inicio = 'A'
pasos = 20
secuencia = proceso_markov(inicio, pasos)
print("Secuencia del proceso de Markov:", secuencia)
