import numpy as np

# Filtro de Kalman (simplificado)
def filtro_kalman(z, x_0, P_0, A, H, Q, R):
    x = x_0
    P = P_0
    resultados = []

    for i in range(len(z)):
        # Predicción
        x_pred = A @ x
        P_pred = A @ P @ A.T + Q

        # Actualización
        K = P_pred @ H.T @ np.linalg.inv(H @ P_pred @ H.T + R)
        x = x_pred + K @ (z[i] - H @ x_pred)
        P = (np.eye(len(K)) - K @ H) @ P_pred

        resultados.append(x)

    return np.array(resultados)

# Parámetros
z = np.array([1.0, 2.0, 3.0])  # Mediciones
x_0 = np.array([0.0])  # Estado inicial
P_0 = np.array([[1]])  # Covarianza inicial
A = np.array([[1]])  # Matriz de transición
H = np.array([[1]])  # Matriz de observación
Q = np.array([[0.1]])  # Covarianza del proceso
R = np.array([[0.1]])  # Covarianza de la observación

# Ejecutar filtro de Kalman
resultados_kalman = filtro_kalman(z, x_0, P_0, A, H, Q, R)
print("Resultados del filtro de Kalman:")
print(resultados_kalman)
