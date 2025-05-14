# Proceso de Decisión de Markov (MDP) resuelto por Iteración de Valores

# Definición de estados
states = ['s0', 's1']  # Dos estados: s0 y s1

# Acciones disponibles en cada estado
actions = ['a0', 'a1']  # Dos acciones: a0 y a1

# Matriz de transición: probabilidad de llegar a s' desde s tomando acción a
T = {
    's0': {
        'a0': {'s0': 0.6, 's1': 0.4},  # Desde s0, acción a0 tiene 60% probabilidad de quedarse en s0 y 40% de ir a s1
        'a1': {'s0': 0.3, 's1': 0.7}   # Desde s0, acción a1 tiene 30% probabilidad de quedarse en s0 y 70% de ir a s1
    },
    's1': {
        'a0': {'s0': 0.8, 's1': 0.2},  # Desde s1, acción a0 tiene 80% de quedarse en s0 y 20% de ir a s1
        'a1': {'s0': 0.4, 's1': 0.6}   # Desde s1, acción a1 tiene 40% de quedarse en s0 y 60% de ir a s1
    }
}

# Recompensas inmediatas por estado y acción
R = {
    's0': {'a0': 4, 'a1': 2},  # Recompensa por acciones en s0
    's1': {'a0': 1, 'a1': 3}   # Recompensa por acciones en s1
}

# Parámetros del MDP
gamma = 0.9  # factor de descuento, cómo valoramos las recompensas futuras
theta = 0.01  # umbral para la convergencia, cuando detener las iteraciones

# Inicialización del valor de cada estado
V = {s: 0 for s in states}  # Empezamos con el valor 0 para todos los estados

def value_iteration():
    """Algoritmo de Iteración de Valores para resolver un MDP"""
    while True:
        delta = 0  # Variable para medir el cambio máximo entre las iteraciones
        for s in states:
            v = V[s]  # Guardamos el valor actual del estado s
            # Se toma el valor máximo sobre todas las acciones posibles
            V[s] = max(
                sum(T[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in states)  # Valor esperado de cada acción
                for a in actions  # Evaluamos cada acción
            )
            delta = max(delta, abs(v - V[s]))  # Actualizamos el cambio máximo entre las iteraciones
        if delta < theta:  # Si el cambio es menor que el umbral, la iteración ha convergido
            break

    # Derivar la política óptima a partir de los valores V
    policy = {}  # Política que asocia cada estado con la acción óptima
    for s in states:
        # Calcular el valor de cada acción posible en el estado s
        action_values = {
            a: sum(T[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in states)
            for a in actions  # Evaluamos cada acción
        }
        policy[s] = max(action_values, key=action_values.get)  # Elegimos la acción con el valor máximo
    return V, policy  # Retornamos los valores de los estados y la política óptima

# Ejecutamos la iteración de valores para obtener la solución
if __name__ == "__main__":
    V_final, policy_final = value_iteration()  # Llamamos a la función para obtener los valores finales y la política óptima
    print("Valores óptimos por estado:")  # Imprimimos los valores finales por estado
    for s in states:
        print(f"  {s}: {V_final[s]:.2f}")  # Mostramos los valores de los estados con 2 decimales
    print("\nPolítica óptima derivada:")  # Imprimimos la política óptima
    for s in states:
        print(f"  En {s} → tomar acción: {policy_final[s]}")  # Mostramos la acción óptima para cada estado
