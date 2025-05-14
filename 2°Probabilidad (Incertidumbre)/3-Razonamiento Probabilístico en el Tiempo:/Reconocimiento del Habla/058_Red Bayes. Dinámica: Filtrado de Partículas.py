import numpy as np  # Importamos numpy para operaciones matemáticas y manejo de arrays

# Definir el modelo del sistema, que simplemente suma un ruido al valor de entrada
def sistema_modelo(x, ruido):
    return x + ruido  # El modelo añade el ruido a la entrada para simular el proceso del sistema

# Filtrado de partículas
def filtrado_particulas(num_particulas, num_iteraciones, ruido_sistema):
    # Inicializamos las partículas en una distribución uniforme entre 0 y 10
    particulas = np.random.uniform(low=0, high=10, size=num_particulas)
    estimacion = []  # Lista para almacenar las estimaciones de cada iteración
    
    # Bucle sobre las iteraciones
    for i in range(num_iteraciones):
        # Actualización de las partículas añadiendo ruido normal a cada partícula
        particulas += np.random.normal(0, ruido_sistema, num_particulas)  # Ruido de proceso (ruido_gaussiano)
        
        # Estimación de la posición media de todas las partículas
        estimacion.append(np.mean(particulas))  # Promedio de las partículas como estimación del estado
        
    return estimacion  # Devuelve las estimaciones obtenidas durante todas las iteraciones

# Parámetros de simulación
num_particulas = 1000  # Número de partículas en el filtro
num_iteraciones = 50  # Número de iteraciones en el filtro
ruido_sistema = 0.1  # Desviación estándar del ruido en el sistema

# Ejecutar el filtrado de partículas
estimaciones = filtrado_particulas(num_particulas, num_iteraciones, ruido_sistema)

# Imprimir las estimaciones obtenidas
print("Estimaciones del filtrado de partículas:", estimaciones)
