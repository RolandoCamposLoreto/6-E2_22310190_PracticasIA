# Importación de la librería numpy para operaciones numéricas
import numpy as np

# Definir la matriz de transición
# La matriz de transición de probabilidades describe cómo cambia el estado del sistema
# dado el estado actual. En este caso, estamos modelando un proceso de Markov para predecir el clima.
transition_probabilities = {
    'Sunny': {'Sunny': 0.8, 'Rainy': 0.2},  # Si está soleado, hay 80% de probabilidad de que siga soleado y 20% de que llueva
    'Rainy': {'Sunny': 0.4, 'Rainy': 0.6}   # Si está lloviendo, hay 40% de probabilidad de que se ponga soleado y 60% de que siga lloviendo
}

# Simulación de un proceso de Markov: Predicción de clima
def markov_process(initial_state, transitions, steps=5):
    """
    Simula un proceso de Markov dado un estado inicial y una matriz de transiciones.
    
    Args:
    - initial_state: Estado inicial del sistema (por ejemplo, 'Sunny').
    - transitions: Diccionario de probabilidades de transición entre estados.
    - steps: Número de pasos a simular.

    Returns:
    - Una lista de estados consecutivos en el proceso de Markov.
    """
    current_state = initial_state  # Establecer el estado inicial
    states = [current_state]       # Lista de estados en el proceso, comenzando con el estado inicial
    for _ in range(steps):
        # Elegir el siguiente estado basado en las probabilidades de transición del estado actual
        next_state = np.random.choice(list(transitions[current_state].keys()), 
                                      p=list(transitions[current_state].values()))
        states.append(next_state)  # Añadir el siguiente estado a la lista
        current_state = next_state  # Actualizar el estado actual al siguiente estado
    return states  # Devolver la secuencia de estados

# Ejemplo de uso: Simular el proceso de Markov comenzando en 'Sunny' y ejecutando 10 pasos
states = markov_process('Sunny', transition_probabilities, steps=10)

# Imprimir la secuencia de estados generados
print("Estados en el proceso de Markov:", states)
