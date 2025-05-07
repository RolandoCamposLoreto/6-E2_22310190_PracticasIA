# Proceso de Decisión de Markov (MDP) resuelto por Iteración de Valores

# Definición de estados
states = ['s0', 's1']

# Acciones disponibles en cada estado
actions = ['a0', 'a1']

# Matriz de transición: probabilidad de llegar a s' desde s tomando acción a
T = {
    's0': {
        'a0': {'s0': 0.6, 's1': 0.4},
        'a1': {'s0': 0.3, 's1': 0.7}
    },
    's1': {
        'a0': {'s0': 0.8, 's1': 0.2},
        'a1': {'s0': 0.4, 's1': 0.6}
    }
}

# Recompensas inmediatas por estado y acción
R = {
    's0': {'a0': 4, 'a1': 2},
    's1': {'a0': 1, 'a1': 3}
}

# Parámetros del MDP
gamma = 0.9  # factor de descuento
theta = 0.01  # umbral para convergencia

# Inicialización del valor de cada estado
V = {s: 0 for s in states}

def value_iteration():
    """Algoritmo de Iteración de Valores para resolver un MDP"""
    while True:
        delta = 0
        for s in states:
            v = V[s]
            # Se toma el valor máximo sobre todas las acciones
            V[s] = max(
                sum(T[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in states)
                for a in actions
            )
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break

    # Derivar la política óptima a partir de los valores V
    policy = {}
    for s in states:
        action_values = {
            a: sum(T[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in states)
            for a in actions
        }
        policy[s] = max(action_values, key=action_values.get)
    return V, policy

if __name__ == "__main__":
    V_final, policy_final = value_iteration()
    print("Valores óptimos por estado:")
    for s in states:
        print(f"  {s}: {V_final[s]:.2f}")
    print("\nPolítica óptima derivada:")
    for s in states:
        print(f"  En {s} → tomar acción: {policy_final[s]}")
