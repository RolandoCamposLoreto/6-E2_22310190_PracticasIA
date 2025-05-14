import numpy as np  # Importamos la librería numpy para trabajar con arrays y funciones matemáticas

# Definir los parámetros del HMM
estados = ['A', 'B']  # Definimos los estados del HMM, en este caso 'A' y 'B'
observaciones = ['X', 'Y']  # Definimos las posibles observaciones, en este caso 'X' y 'Y'
# Matriz de probabilidades de transición entre estados
transiciones = np.array([[0.7, 0.3],  # Probabilidad de transición de A -> A (0.7) y A -> B (0.3)
                         [0.4, 0.6]])  # Probabilidad de transición de B -> A (0.4) y B -> B (0.6)

# Matriz de probabilidades de emisión: Probabilidades de observar X o Y dado el estado
emisiones = np.array([[0.5, 0.5],  # Probabilidad de observar X (0.5) o Y (0.5) dado el estado A
                      [0.1, 0.9]])  # Probabilidad de observar X (0.1) o Y (0.9) dado el estado B

# Inicializar las probabilidades de los estados en el tiempo inicial
prob_inicial = np.array([0.5, 0.5])  # Las probabilidades de inicio de A y B, ambos con probabilidad 0.5

# Secuencia de observaciones
sec_observacion = ['X', 'Y', 'X']  # Secuencia de observaciones que el modelo debe evaluar

# Convertir las observaciones a índices para facilitar el acceso a las matrices
observaciones_idx = [0, 1, 0]  # 'X' se convierte en 0, 'Y' en 1, y 'X' nuevamente en 0

# Algoritmo hacia adelante (Forward Algorithm)
def forward_algorithm(observaciones_idx, transiciones, emisiones, prob_inicial):
    n_estados = len(estados)  # Número de estados en el HMM
    n_observaciones = len(observaciones_idx)  # Número de observaciones en la secuencia
    
    # Inicializar la matriz alfa, que almacenará las probabilidades hacia adelante
    alfa = np.zeros((n_observaciones, n_estados))
    
    # Inicialización: Probabilidades para el primer paso
    alfa[0, :] = prob_inicial * emisiones[:, observaciones_idx[0]]  # Multiplicamos la probabilidad inicial por las emisiones correspondientes
    
    # Recursión: Calculamos las probabilidades hacia adelante para cada observación
    for t in range(1, n_observaciones):  # Para cada observación a partir de la segunda
        for j in range(n_estados):  # Para cada estado
            # Calculamos la probabilidad hacia adelante para el estado j en el tiempo t
            alfa[t, j] = np.sum(alfa[t-1, :] * transiciones[:, j]) * emisiones[j, observaciones_idx[t]]
    
    return alfa  # Devolvemos la matriz de probabilidades hacia adelante

# Ejecutar el algoritmo hacia adelante
alfa = forward_algorithm(observaciones_idx, transiciones, emisiones, prob_inicial)

# Imprimir los resultados
print("Probabilidades hacia adelante (Forward):")
print(alfa)  # Mostramos la matriz de probabilidades hacia adelante para cada observación y estado
