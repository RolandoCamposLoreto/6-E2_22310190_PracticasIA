import numpy as np  # Importamos numpy para trabajar con arrays y funciones matemáticas

# Parámetros de un modelo oculto de Markov
estados = ['A', 'B']  # Definimos los posibles estados del modelo, en este caso 'A' y 'B'
observaciones = ['X', 'Y']  # Definimos las observaciones posibles, 'X' y 'Y'
# Matriz de probabilidades de transición: probabilidades de pasar de un estado a otro
transiciones = np.array([[0.7, 0.3],  # Probabilidad de transición de A -> A (0.7) y A -> B (0.3)
                         [0.4, 0.6]])  # Probabilidad de transición de B -> A (0.4) y B -> B (0.6)

# Matriz de probabilidades de emisión: Probabilidades de observar 'X' o 'Y' dado el estado
emisiones = np.array([[0.5, 0.5],  # Probabilidad de observar 'X' (0.5) o 'Y' (0.5) dado el estado 'A'
                      [0.1, 0.9]])  # Probabilidad de observar 'X' (0.1) o 'Y' (0.9) dado el estado 'B'

# Probabilidades iniciales: La probabilidad de que el modelo inicie en cada uno de los estados
prob_inicial = np.array([0.5, 0.5])  # Estado inicial con probabilidad 0.5 para 'A' y 0.5 para 'B'

# Secuencia de observaciones (es decir, las observaciones que recibimos)
sec_observacion = ['X', 'Y', 'X']  # Secuencia de observaciones, por ejemplo: 'X', 'Y', 'X'

# Convertir las observaciones a índices para facilitar el cálculo
observaciones_idx = [0, 1, 0]  # 'X' se convierte en 0 y 'Y' en 1 (de acuerdo con el orden en 'observaciones')

# Función para el algoritmo hacia adelante (Forward Algorithm)
def forward_algorithm(observaciones_idx, transiciones, emisiones, prob_inicial):
    n_estados = len(estados)  # Número de estados en el modelo HMM
    n_observaciones = len(observaciones_idx)  # Número de observaciones en la secuencia
    
    # Inicializar la matriz alfa, que almacenará las probabilidades hacia adelante
    alfa = np.zeros((n_observaciones, n_estados))
    
    # Inicialización del primer paso: Probabilidad de estar en cada estado dado la primera observación
    alfa[0, :] = prob_inicial * emisiones[:, observaciones_idx[0]]
    
    # Recursión para calcular las probabilidades hacia adelante en cada paso de la secuencia
    for t in range(1, n_observaciones):  # Para cada observación a partir de la segunda
        for j in range(n_estados):  # Para cada estado en el que el proceso puede estar
            # Calculamos la probabilidad hacia adelante para el estado 'j' en el tiempo 't'
            alfa[t, j] = np.sum(alfa[t-1, :] * transiciones[:, j]) * emisiones[j, observaciones_idx[t]]
    
    return alfa  # Devolvemos la matriz de probabilidades hacia adelante

# Ejecutar el algoritmo hacia adelante con los parámetros dados
alfa = forward_algorithm(observaciones_idx, transiciones, emisiones, prob_inicial)

# Imprimir los resultados
print("Probabilidades hacia adelante (Forward):")
print(alfa)  # Mostramos la matriz 'alfa', que contiene las probabilidades hacia adelante en cada paso
