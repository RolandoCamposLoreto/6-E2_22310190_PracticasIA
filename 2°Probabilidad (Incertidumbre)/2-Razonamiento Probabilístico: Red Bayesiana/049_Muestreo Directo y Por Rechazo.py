import numpy as np

# Muestreo directo de una distribución uniforme
samples = np.random.uniform(low=0, high=1, size=1000)
print(f"Muestras directas: {samples[:10]}")

# Muestreo por rechazo (Rechazo de valores fuera de un intervalo dado)
def rejection_sampling(target_dist, proposal_dist, proposal_params, n_samples):
    samples = []
    while len(samples) < n_samples:
        sample = proposal_dist(*proposal_params)
        u = np.random.uniform(0, 1)
        if u < target_dist(sample) / proposal_dist(sample):
            samples.append(sample)
    return samples

# Usar muestreo por rechazo para obtener valores de una distribución normal
target_dist = lambda x: np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)
proposal_dist = np.random.normal
proposal_params = (0, 1)
rejected_samples = rejection_sampling(target_dist, proposal_dist, proposal_params, 1000)
print(f"Muestras por rechazo: {rejected_samples[:10]}")
