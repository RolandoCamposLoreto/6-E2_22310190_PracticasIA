import numpy as np  # Importamos numpy para manejar matrices y operaciones matemáticas

# Función para aplicar el filtro de Kalman (simplificado)
def filtro_kalman(z, x_0, P_0, A, H, Q, R):
    x = x_0  # Estado inicial
    P = P_0  # Covarianza inicial
    resultados = []  # Lista para almacenar los resultados (estados estimados)

    # Bucle a través de las mediciones z
    for i in range(len(z)):
        # Predicción del siguiente estado
        x_pred = A @ x  # Predicción del estado utilizando la matriz de transición A
        P_pred = A @ P @ A.T + Q  # Predicción de la covarianza

        # Cálculo de la ganancia de Kalman
        K = P_pred @ H.T @ np.linalg.inv(H @ P_pred @ H.T + R)  # Ganancia de Kalman

        # Actualización del estado y la covarianza con la medición z[i]
        x = x_pred + K @ (z[i] - H @ x_pred)  # Actualización del estado
        P = (np.eye(len(K)) - K @ H) @ P_pred  # Actualización de la covarianza

        resultados.append(x)  # Guardamos el estado estimado

    return np.array(resultados)  # Convertimos la lista de resultados a un array numpy para devolverla

# Parámetros del filtro de Kalman
z = np.array([1.0, 2.0, 3.0])  # Mediciones obtenidas
x_0 = np.array([0.0])  # Estado inicial (por ejemplo, 0)
P_0 = np.array([[1]])  # Covarianza inicial (asumimos incertidumbre inicial)
A = np.array([[1]])  # Matriz de transición del estado (modelo del sistema)
H = np.array([[1]])  # Matriz de observación (como las mediciones directamente nos dan el estado)
Q = np.array([[0.1]])  # Covarianza del proceso (ruido en el proceso)
R = np.array([[0.1]])  # Covarianza de la medición (ruido en las mediciones)

# Ejecutar filtro de Kalman
resultados_kalman = filtro_kalman(z, x_0, P_0, A, H, Q, R)

# Mostrar los resultados
print("Resultados del filtro de Kalman:")
print(resultados_kalman)  # Imprime el estado estimado después de cada medición
