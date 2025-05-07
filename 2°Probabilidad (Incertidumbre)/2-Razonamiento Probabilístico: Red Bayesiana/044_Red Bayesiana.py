import numpy as np

# Definir las probabilidades a priori y condicionales
P_rain = np.array([0.7, 0.3])  # Probabilidad de lluvia [No, Sí]
P_traffic_given_rain = np.array([[0.8, 0.2],  # Si no llueve: [No tráfico, Tráfico]
                                 [0.4, 0.6]]) # Si llueve: [No tráfico, Tráfico]

P_accident_given_traffic = np.array([[0.9, 0.1],  # Si no hay tráfico: [Accidente, No accidente]
                                     [0.6, 0.4]]) # Si hay tráfico: [Accidente, No accidente]

# Función de inferencia para el accidente dado la lluvia
def inferencia_accidente(P_rain, P_traffic_given_rain, P_accident_given_traffic):
    # Inferencia para tráfico dado lluvia
    P_traffic = np.dot(P_rain, P_traffic_given_rain)

    # Inferencia para accidente dado tráfico
    P_accident = np.dot(P_traffic, P_accident_given_traffic)
    
    return P_accident

# Obtener la probabilidad de un accidente dado que llueve
P_accidente_dado_lluvia = inferencia_accidente(P_rain, P_traffic_given_rain, P_accident_given_traffic)
print(f"Probabilidad de un accidente dado que llueve: {P_accidente_dado_lluvia[1]:.2f}")
