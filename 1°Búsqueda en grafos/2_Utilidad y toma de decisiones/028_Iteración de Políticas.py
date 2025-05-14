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

# Parámetros del MDP
gamma = 0.9  # Factor de descuento.
theta = 0.01  # Umbral de convergencia.

# Inicializamos política aleatoria y valores V
policy = {s: 'a0' for s in states}  # Política inicial aleatoria, donde se elige a0 por defecto.
V = {s: 0 for s in states}  # Inicializamos los valores de los estados a 0.

def policy_evaluation(policy, V):
    """Evalúa una política fija hasta convergencia."""
    while True:
        delta = 0  # Para calcular el cambio máximo entre iteraciones.
        for s in states:
            v = V[s]  # Guardamos el valor antiguo del estado.
            a = policy[s]  # Acción tomada según la política actual.
            # Evaluamos el valor del estado sumando las probabilidades de transición y las recompensas.
            V[s] = sum(T[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in states)
            delta = max(delta, abs(v - V[s]))  # Calculamos el cambio máximo en los valores.
        if delta < theta:  # Si el cambio es menor que el umbral, hemos alcanzado la convergencia.
            break
    return V

def policy_improvement(V, policy):
    """Mejora la política basada en los valores actuales."""
    policy_stable = True  # Asumimos que la política es estable hasta demostrar lo contrario.
    for s in states:
        old_action = policy[s]  # Acción anterior en el estado.
        # Calculamos el valor de cada acción en el estado s.
        action_values = {
            a: sum(T[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in states)
            for a in actions
        }
        # Elegimos la acción que da el mayor valor esperado.
        best_action = max(action_values, key=action_values.get)
        policy[s] = best_action  # Actualizamos la política.
        if old_action != best_action:  # Si la acción cambia, la política no es estable.
            policy_stable = False
    return policy_stable, policy

def policy_iteration():
    global V, policy  # Usamos las variables globales V y policy.
    while True:
        V = policy_evaluation(policy, V)  # Evaluamos la política actual.
        stable, policy = policy_improvement(V, policy)  # Mejoramos la política.
        if stable:  # Si la política es estable, hemos terminado.
            break
    return V, policy

if __name__ == "__main__":
    V_final, policy_final = policy_iteration()  # Ejecutamos la iteración de políticas.
    print("Valores óptimos por estado:")
    for s, v in V_final.items():
        print(f"  {s}: {v:.2f}")  # Imprimimos los valores finales de cada estado.

    print("\nPolítica óptima:")
    for s, a in policy_final.items():
        print(f"  En {s} → tomar acción: {a}")  # Imprimimos la política óptima.
