import numpy as np

# Parámetros de un modelo oculto de Markov
estados = ['A', 'B']
observaciones = ['X', 'Y']
transiciones = np.array([[0.7, 0.3],  # Probabilidades de transición
                         [0.4, 0.6]])

emisiones = np.array([[0.5, 0.5],  # Probabilidades de observación
                      [0.1, 0.9]])

prob_inicial = np.array([0.5, 0.5])  # Probabilidades iniciales

# Secuencia de observaciones
sec_observacion = ['X', 'Y', 'X']

# Convertir las observaciones a índices
observaciones_idx = [0, 1, 0]  # X -> 0, Y -> 1, X -> 0

# Función para el algoritmo hacia adelante (Forward)
def forward_algorithm(observaciones_idx, transiciones, emisiones, prob_inicial):
    n_estados = len(estados)
    n_observaciones = len(observaciones_idx)
    
    # Inicializar la matriz alfa
    alfa = np.zeros((n_observaciones, n_estados))
    
    # Inicialización (primer paso)
    alfa[0, :] = prob_inicial * emisiones[:, observaciones_idx[0]]
    
    # Recursión (pasos siguientes)
    for t in range(1, n_observaciones):
        for j in range(n_estados):
            alfa[t, j] = np.sum(alfa[t-1, :] * transiciones[:, j]) * emisiones[j, observaciones_idx[t]]
    
    return alfa

# Ejecutar el algoritmo hacia adelante
alfa = forward_algorithm(observaciones_idx, transiciones, emisiones, prob_inicial)
print("Probabilidades hacia adelante (Forward):")
print(alfa)
