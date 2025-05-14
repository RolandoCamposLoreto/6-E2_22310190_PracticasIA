# MDP Parcialmente Observable (POMDP) - Ejemplo básico

# Definición de estados, acciones y observaciones
states = ['s0', 's1']  # Dos estados posibles: s0 y s1
actions = ['a0', 'a1']  # Dos acciones posibles: a0 y a1
observations = ['o0', 'o1']  # Dos posibles observaciones: o0 y o1

# Probabilidad de transición T[s][a][s']: 
# Probabilidad de ir del estado s a s' tomando la acción a
T = {
    's0': {
        'a0': {'s0': 0.7, 's1': 0.3},  # Desde s0, acción a0 tiene 70% probabilidad de quedarse en s0 y 30% de ir a s1
        'a1': {'s0': 0.4, 's1': 0.6}   # Desde s0, acción a1 tiene 40% probabilidad de quedarse en s0 y 60% de ir a s1
    },
    's1': {
        'a0': {'s0': 0.5, 's1': 0.5},  # Desde s1, acción a0 tiene 50% probabilidad de quedarse en s0 y 50% de ir a s1
        'a1': {'s0': 0.6, 's1': 0.4}   # Desde s1, acción a1 tiene 60% probabilidad de quedarse en s0 y 40% de ir a s1
    }
}

# Probabilidad de observación O[s][a][o]: 
# Probabilidad de observar o dado que tomamos acción a en el estado s
O = {
    's0': {
        'a0': {'o0': 0.8, 'o1': 0.2},  # Desde s0, acción a0 tiene 80% de observar o0 y 20% de observar o1
        'a1': {'o0': 0.5, 'o1': 0.5}   # Desde s0, acción a1 tiene 50% de observar o0 y 50% de observar o1
    },
    's1': {
        'a0': {'o0': 0.4, 'o1': 0.6},  # Desde s1, acción a0 tiene 40% de observar o0 y 60% de observar o1
        'a1': {'o0': 0.9, 'o1': 0.1}   # Desde s1, acción a1 tiene 90% de observar o0 y 10% de observar o1
    }
}

# Recompensas R[s][a]: recompensa inmediata por tomar la acción a en el estado s
R = {
    's0': {'a0': 5, 'a1': 2},  # Recompensas para las acciones en s0
    's1': {'a0': -1, 'a1': 3}  # Recompensas para las acciones en s1
}

# Parámetros
gamma = 0.9  # Factor de descuento, como valoramos las recompensas futuras
theta = 0.01  # Umbral para la convergencia, cuando parar la iteración de valores

# Inicialización de creencias y valores
belief = {'s0': 0.5, 's1': 0.5}  # Creencia inicial sobre el estado (probabilidad de estar en s0 o s1)
V = {s: 0 for s in states}  # Inicialización de los valores de los estados en 0

# Definimos la función de iteración de valores para un POMDP
def pomdp_value_iteration():
    """Algoritmo de Iteración de Valores para POMDP"""
    
    # Inicia el proceso iterativo de actualización de valores de los estados
    while True:
        delta = 0  # Variable para medir el cambio máximo entre iteraciones
        for s in states:
            v = V[s]  # Guardamos el valor actual del estado s
            
            # Calculamos el valor máximo sobre todas las acciones posibles, considerando la creencia
            V[s] = max(
                sum(T[s][a][s_prime] * (R[s][a] + gamma * belief[s_prime] * V[s_prime]) for s_prime in states)
                for a in actions  # Evaluamos cada acción posible (a0 y a1)
            )
            
            # Comprobamos el máximo cambio en los valores de los estados entre iteraciones
            delta = max(delta, abs(v - V[s]))
        
        # Si el cambio máximo es menor que el umbral de convergencia, detenemos la iteración
        if delta < theta:
            break

    # Derivamos la política óptima basada en la creencia (que acción tomar en cada estado)
    policy = {}  # Diccionario para almacenar la política óptima
    for s in states:
        # Calculamos el valor de cada acción posible en el estado s
        action_values = {
            a: sum(T[s][a][s_prime] * (R[s][a] + gamma * belief[s_prime] * V[s_prime]) for s_prime in states)
            for a in actions  # Evaluamos cada acción posible
        }
        
        # Asignamos la acción óptima al estado s, es decir, la que maximiza el valor
        policy[s] = max(action_values, key=action_values.get)
    
    return V, policy  # Devolvemos los valores de los estados y la política óptima

# Ejecutamos la iteración de valores para obtener la solución
if __name__ == "__main__":
    V_final, policy_final = pomdp_value_iteration()  # Llamamos a la función para obtener los valores finales y la política óptima
    
    # Imprimimos los valores óptimos de cada estado
    print("Valores óptimos por estado:")
    for s in states:
        print(f"  {s}: {V_final[s]:.2f}")  # Mostramos los valores con 2 decimales
    
    # Imprimimos la política óptima derivada
    print("\nPolítica óptima derivada:")
    for s in states:
        print(f"  En {s} → tomar acción: {policy_final[s]}")  # Mostramos la acción óptima para cada estado
