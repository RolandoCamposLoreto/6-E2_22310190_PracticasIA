import random  # Importamos la librería random para realizar selecciones aleatorias

# Definir los estados de Markov y las probabilidades de transición
# Los estados posibles en el proceso de Markov son 'A' y 'B'
# Las transiciones de un estado a otro están definidas con las probabilidades correspondientes
estados = ['A', 'B']
transiciones = {
    'A': {'A': 0.7, 'B': 0.3},  # Si estamos en el estado A, la probabilidad de permanecer en A es 0.7, y de ir a B es 0.3
    'B': {'A': 0.4, 'B': 0.6}   # Si estamos en el estado B, la probabilidad de ir a A es 0.4, y de permanecer en B es 0.6
}

# Función para simular un proceso de Markov
# Este proceso toma un estado inicial y genera una secuencia de estados basada en las transiciones definidas
def proceso_markov(inicio, pasos):
    estado_actual = inicio  # El estado actual comienza siendo el estado de inicio
    secuencia = [estado_actual]  # Inicializamos la secuencia con el estado de inicio
    
    # Realizamos la simulación del proceso durante un número de pasos
    for _ in range(pasos):
        # Elegimos el siguiente estado basándonos en las probabilidades de transición desde el estado actual
        # random.choices toma una lista de posibles estados (estados) y sus probabilidades (weights)
        estado_actual = random.choices(estados, weights=[transiciones[estado_actual]['A'], transiciones[estado_actual]['B']])[0]
        secuencia.append(estado_actual)  # Añadimos el nuevo estado a la secuencia
    
    return secuencia  # Devolvemos la secuencia de estados generada

# Simulación del proceso de Markov
inicio = 'A'  # El proceso comienza en el estado 'A'
pasos = 20  # Número de pasos a simular
secuencia = proceso_markov(inicio, pasos)  # Generamos la secuencia de estados
print("Secuencia del proceso de Markov:", secuencia)  # Imprimimos la secuencia generada
