import numpy as np

# Definir el modelo del sistema
def sistema_modelo(x, ruido):
    return x + ruido

# Filtrado de partículas
def filtrado_particulas(num_particulas, num_iteraciones, ruido_sistema):
    particulas = np.random.uniform(low=0, high=10, size=num_particulas)
    estimacion = []
    
    for i in range(num_iteraciones):
        particulas += np.random.normal(0, ruido_sistema, num_particulas)  # Actualizar con ruido
        estimacion.append(np.mean(particulas))  # Estimación como la media de las partículas

    return estimacion

# Parámetros
num_particulas = 1000
num_iteraciones = 50
ruido_sistema = 0.1

# Ejecutar el filtrado de partículas
estimaciones = filtrado_particulas(num_particulas, num_iteraciones, ruido_sistema)
print("Estimaciones del filtrado de partículas:", estimaciones)
