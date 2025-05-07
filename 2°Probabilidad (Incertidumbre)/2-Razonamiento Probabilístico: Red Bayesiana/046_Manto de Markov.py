import numpy as np

# Definir la matriz de transición
transition_probabilities = {
    'Sunny': {'Sunny': 0.8, 'Rainy': 0.2},
    'Rainy': {'Sunny': 0.4, 'Rainy': 0.6}
}

# Simulación de un proceso de Markov: Predicción de clima
def markov_process(initial_state, transitions, steps=5):
    current_state = initial_state
    states = [current_state]
    for _ in range(steps):
        next_state = np.random.choice(list(transitions[current_state].keys()), 
                                      p=list(transitions[current_state].values()))
        states.append(next_state)
        current_state = next_state
    return states

# Ejemplo de uso
states = markov_process('Sunny', transition_probabilities, steps=10)
print("Estados en el proceso de Markov:", states)
