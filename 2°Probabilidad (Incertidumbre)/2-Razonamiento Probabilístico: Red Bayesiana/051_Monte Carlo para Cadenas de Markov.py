import numpy as np

# Definir una función para el muestreo MCMC (Cadenas de Markov)
def metropolis_hastings(target_dist, proposal_dist, proposal_params, n_samples, initial_state):
    samples = [initial_state]
    current_state = initial_state
    
    for _ in range(n_samples):
        proposed_state = proposal_dist(*proposal_params)
        acceptance_ratio = min(1, target_dist(proposed_state) / target_dist(current_state))
        
        if np.random.uniform(0, 1) < acceptance_ratio:
            current_state = proposed_state
        
        samples.append(current_state)
    
    return np.array(samples)

# Definir la distribución objetivo (distribución normal)
target_dist = lambda x: np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)

# Definir la distribución propuesta (distribución normal centrada)
proposal_dist = np.random.normal
proposal_params = (0, 1)
initial_state = 0

# Muestreo MCMC
samples = metropolis_hastings(target_dist, proposal_dist, proposal_params, 1000, initial_state)

# Graficar los resultados
import matplotlib.pyplot as plt
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')
plt.title("Muestreo MCMC")
plt.show()
