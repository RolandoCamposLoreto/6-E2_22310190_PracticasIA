# Importar la librería numpy, que se utiliza para trabajar con arreglos y funciones matemáticas
import numpy as np

# Muestreo directo de una distribución uniforme
# Generamos muestras aleatorias de una distribución uniforme en el intervalo [0, 1]
samples = np.random.uniform(low=0, high=1, size=1000)  # 1000 muestras
# Imprimimos las primeras 10 muestras para verificar
print(f"Muestras directas: {samples[:10]}")

# Función de muestreo por rechazo (Rechazo de valores fuera de un intervalo dado)
# Esta técnica permite generar muestras de una distribución target utilizando una distribución de propuesta
def rejection_sampling(target_dist, proposal_dist, proposal_params, n_samples):
    samples = []  # Lista para almacenar las muestras aceptadas
    while len(samples) < n_samples:
        # Generamos una muestra de la distribución propuesta
        sample = proposal_dist(*proposal_params)
        # Generamos un valor aleatorio entre 0 y 1
        u = np.random.uniform(0, 1)
        # Aceptamos la muestra si cumple con la condición de probabilidad
        if u < target_dist(sample) / proposal_dist(sample):
            samples.append(sample)  # Añadimos la muestra a la lista
    return samples

# Usar muestreo por rechazo para obtener valores de una distribución normal
# Definimos la distribución target, que es la normal estándar (con media 0 y desviación estándar 1)
target_dist = lambda x: np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)  # PDF de la normal estándar
# Usamos la distribución normal estándar como propuesta
proposal_dist = np.random.normal
# Los parámetros de la distribución normal son media 0 y desviación estándar 1
proposal_params = (0, 1)
# Aplicamos el muestreo por rechazo para obtener 1000 muestras
rejected_samples = rejection_sampling(target_dist, proposal_dist, proposal_params, 1000)
# Imprimimos las primeras 10 muestras generadas por el muestreo por rechazo
print(f"Muestras por rechazo: {rejected_samples[:10]}")
