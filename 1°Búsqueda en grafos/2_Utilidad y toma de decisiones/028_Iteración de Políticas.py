# Iteración de Políticas para un MDP simple
# Ejecutable directamente desde un entorno local o GitHub

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

# Parámetros del MDP
gamma = 0.9
theta = 0.01

# Inicializamos política aleatoria y valores V
policy = {s: 'a0' for s in states}
V = {s: 0 for s in states}

def policy_evaluation(policy, V):
    """Evalúa una política fija hasta convergencia."""
    while True:
        delta = 0
        for s in states:
            v = V[s]
            a = policy[s]
            V[s] = sum(T[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in states)
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break
    return V

def policy_improvement(V, policy):
    """Mejora la política basada en los valores actuales."""
    policy_stable = True
    for s in states:
        old_action = policy[s]
        # Calcular valor de cada acción
        action_values = {
            a: sum(T[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in states)
            for a in actions
        }
        best_action = max(action_values, key=action_values.get)
        policy[s] = best_action
        if old_action != best_action:
            policy_stable = False
    return policy_stable, policy

def policy_iteration():
    global V, policy
    while True:
        V = policy_evaluation(policy, V)
        stable, policy = policy_improvement(V, policy)
        if stable:
            break
    return V, policy

if __name__ == "__main__":
    V_final, policy_final = policy_iteration()
    print("Valores óptimos por estado:")
    for s, v in V_final.items():
        print(f"  {s}: {v:.2f}")
    print("\nPolítica óptima:")
    for s, a in policy_final.items():
        print(f"  En {s} → tomar acción: {a}")
