# MDP Parcialmente Observable (POMDP) - Ejemplo básico

# Definición de estados, acciones y observaciones
states = ['s0', 's1']
actions = ['a0', 'a1']
observations = ['o0', 'o1']

# Probabilidad de transición T[s][a][s']
T = {
    's0': {
        'a0': {'s0': 0.7, 's1': 0.3},
        'a1': {'s0': 0.4, 's1': 0.6}
    },
    's1': {
        'a0': {'s0': 0.5, 's1': 0.5},
        'a1': {'s0': 0.6, 's1': 0.4}
    }
}

# Probabilidad de observación O[s][a][o]
O = {
    's0': {
        'a0': {'o0': 0.8, 'o1': 0.2},
        'a1': {'o0': 0.5, 'o1': 0.5}
    },
    's1': {
        'a0': {'o0': 0.4, 'o1': 0.6},
        'a1': {'o0': 0.9, 'o1': 0.1}
    }
}

# Recompensas R[s][a]
R = {
    's0': {'a0': 5, 'a1': 2},
    's1': {'a0': -1, 'a1': 3}
}

# Parámetros
gamma = 0.9
theta = 0.01

# Inicialización de creencias y valores
belief = {'s0': 0.5, 's1': 0.5}  # Creencia inicial sobre el estado
V = {s: 0 for s in states}

def pomdp_value_iteration():
    """Algoritmo de Iteración de Valores para POMDP"""
    while True:
        delta = 0
        for s in states:
            v = V[s]
            # Valor máximo de todas las acciones considerando la creencia
            V[s] = max(
                sum(T[s][a][s_prime] * (R[s][a] + gamma * belief[s_prime] * V[s_prime]) for s_prime in states)
                for a in actions
            )
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break

    # Derivar la política óptima basada en la creencia
    policy = {}
    for s in states:
        action_values = {
            a: sum(T[s][a][s_prime] * (R[s][a] + gamma * belief[s_prime] * V[s_prime]) for s_prime in states)
            for a in actions
        }
        policy[s] = max(action_values, key=action_values.get)
    return V, policy

if __name__ == "__main__":
    V_final, policy_final = pomdp_value_iteration()
    print("Valores óptimos por estado:")
    for s in states:
        print(f"  {s}: {V_final[s]:.2f}")
    print("\nPolítica óptima derivada:")
    for s in states:
        print(f"  En {s} → tomar acción: {policy_final[s]}")
