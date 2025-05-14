# Importar la librería numpy para operaciones matemáticas y generación de números aleatorios
import numpy as np

# Definir una función para el muestreo MCMC utilizando el algoritmo de Metropolis-Hastings
def metropolis_hastings(target_dist, proposal_dist, proposal_params, n_samples, initial_state):
    # Inicializamos la lista de muestras con el estado inicial
    samples = [initial_state]
    current_state = initial_state
    
    # Iteramos para obtener las muestras
    for _ in range(n_samples):
        # Proponemos un nuevo estado utilizando la distribución propuesta
        proposed_state = proposal_dist(*proposal_params)
        
        # Calculamos la razón de aceptación (proporción de la verosimilitud)
        acceptance_ratio = min(1, target_dist(proposed_state) / target_dist(current_state))
        
        # Aceptamos o rechazamos el nuevo estado basado en la razón de aceptación
        if np.random.uniform(0, 1) < acceptance_ratio:
            current_state = proposed_state
        
        # Añadimos el estado actual a la lista de muestras
        samples.append(current_state)
    
    return np.array(samples)  # Retornamos las muestras generadas

# Definir la distribución objetivo (en este caso, una distribución normal estándar)
target_dist = lambda x: np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)  # Distribución normal estándar

# Definir la distribución propuesta (en este caso, una distribución normal centrada en 0 con desviación estándar 1)
proposal_dist = np.random.normal  # Distribución normal estándar
proposal_params = (0, 1)  # Parámetros de la distribución normal propuesta (media=0, desviación estándar=1)
initial_state = 0  # Estado inicial para el muestreo

# Ejecutar el muestreo MCMC para generar 1000 muestras
samples = metropolis_hastings(target_dist, proposal_dist, proposal_params, 1000, initial_state)

# Importar matplotlib para graficar los resultados
import matplotlib.pyplot as plt
# Graficar el histograma de las muestras generadas por el muestreo MCMC
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')  # Histograma con 30 bins, densidad normalizada
plt.title("Muestreo MCMC")  # Título del gráfico
plt.show()  # Mostrar el gráfico
