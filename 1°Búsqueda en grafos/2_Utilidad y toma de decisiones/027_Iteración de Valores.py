# Iteración de Valores para un MDP simple
# Compatible con ejecución desde GitHub o entorno local

# Estados del entorno
states = ['s0', 's1']

# Acciones posibles
actions = ['a0', 'a1']

# Matriz de transición T[s][a][s'] = probabilidad
T = {
    's0': {
        'a0': {'s0': 0.5, 's1': 0.5},
        'a1': {'s0': 0.2, 's1': 0.8}
    },
    's1': {
        'a0': {'s0': 0.7, 's1': 0.3},
        'a1': {'s0': 0.4, 's1': 0.6}
    }
}

# Recompensas inmediatas R[s][a]
R = {
    's0': {'a0': 5, 'a1': 10},
    's1': {'a0': -1, 'a1': 2}
}

# Parámetros
gamma = 0.9  # factor de descuento
theta = 0.01  # umbral para convergencia

# Inicializamos valores V[s] = 0
V = {s: 0 for s in states}

def value_iteration():
    while True:
        delta = 0
        for s in states:
            v = V[s]
            # Evaluamos cada acción y elegimos el mejor valor esperado
            V[s] = max(
                sum(T[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in states)
                for a in actions
            )
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break

    # Política óptima: para cada estado, elegimos la mejor acción
    policy = {}
    for s in states:
        best_action = max(actions, key=lambda a: sum(
            T[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in states
        ))
        policy[s] = best_action
    return V, policy

if __name__ == "__main__":
    V_final, policy_optima = value_iteration()
    print("Valores óptimos por estado:")
    for s, v in V_final.items():
        print(f"  {s}: {v:.2f}")
    print("\nPolítica óptima:")
    for s, a in policy_optima.items():
        print(f"  En {s} → tomar acción: {a}")
