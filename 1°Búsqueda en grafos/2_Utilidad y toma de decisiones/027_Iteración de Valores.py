# Estados del entorno
states = ['s0', 's1']  # Definimos dos estados: s0 y s1.

# Acciones posibles
actions = ['a0', 'a1']  # Definimos dos acciones: a0 y a1.

# Matriz de transición T[s][a][s'] = probabilidad
# Esta matriz describe las probabilidades de transición entre los estados, dadas las acciones.
T = {
    's0': {
        'a0': {'s0': 0.5, 's1': 0.5},  # Si estamos en s0 y tomamos la acción a0, hay un 50% de probabilidad de quedarse en s0 o ir a s1.
        'a1': {'s0': 0.2, 's1': 0.8}   # Si estamos en s0 y tomamos la acción a1, hay un 20% de probabilidad de quedarse en s0 o ir a s1.
    },
    's1': {
        'a0': {'s0': 0.7, 's1': 0.3},  # Si estamos en s1 y tomamos la acción a0, hay un 70% de probabilidad de ir a s0 o quedarse en s1.
        'a1': {'s0': 0.4, 's1': 0.6}   # Si estamos en s1 y tomamos la acción a1, hay un 40% de probabilidad de ir a s0 o quedarse en s1.
    }
}

# Recompensas inmediatas R[s][a]
# Define las recompensas inmediatas por cada par (estado, acción).
R = {
    's0': {'a0': 5, 'a1': 10},  # Recompensas para las acciones en el estado s0.
    's1': {'a0': -1, 'a1': 2}   # Recompensas para las acciones en el estado s1.
}

# Parámetros
gamma = 0.9  # Factor de descuento: la importancia de las recompensas futuras.
theta = 0.01  # Umbral de convergencia: si el cambio en los valores es menor a este valor, la iteración termina.

# Inicializamos los valores V[s] = 0 para todos los estados
V = {s: 0 for s in states}  # Los valores iniciales de los estados son 0.

# Función de Iteración de Valores
def value_iteration():
    while True:
        delta = 0  # Variable para calcular el cambio máximo entre iteraciones
        for s in states:
            v = V[s]  # Guardamos el valor anterior del estado
            # Evaluamos cada acción y elegimos el mejor valor esperado
            V[s] = max(
                sum(T[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in states)  # Valor esperado de tomar una acción.
                for a in actions
            )
            delta = max(delta, abs(v - V[s]))  # Calculamos el máximo cambio en los valores de los estados
        if delta < theta:  # Si el cambio es menor al umbral, se ha alcanzado la convergencia
            break

    # Política óptima: para cada estado, elegimos la mejor acción
    policy = {}
    for s in states:
        # Elegimos la acción que da el mayor valor esperado
        best_action = max(actions, key=lambda a: sum(
            T[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in states
        ))
        policy[s] = best_action  # Asignamos la mejor acción a cada estado
    return V, policy  # Retornamos los valores óptimos y la política óptima

# Ejecución del programa principal
if __name__ == "__main__":
    V_final, policy_optima = value_iteration()  # Ejecutamos la iteración de valores para encontrar los valores y la política óptima.
    
    # Imprimimos los resultados
    print("Valores óptimos por estado:")
    for s, v in V_final.items():
        print(f"  {s}: {v:.2f}")  # Imprimimos los valores finales por estado.

    print("\nPolítica óptima:")
    for s, a in policy_optima.items():
        print(f"  En {s} → tomar acción: {a}")  # Imprimimos la acción óptima por cada estado.
