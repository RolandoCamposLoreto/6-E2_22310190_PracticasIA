import numpy as np

# Función para calcular la paridad
def hamming_encode(bits):
    """
    Codifica un mensaje de 4 bits con el código de Hamming de 7 bits
    """
    # Generar la matriz de paridad
    G = np.array([[1, 1, 0, 1], 
                  [1, 0, 1, 1], 
                  [1, 0, 0, 0], 
                  [0, 1, 1, 1], 
                  [0, 1, 0, 0], 
                  [0, 0, 1, 0], 
                  [0, 0, 0, 1]])
    # Codificación del mensaje de 4 bits a 7 bits
    return np.dot(bits, G) % 2

# Ejemplo de uso
message = np.array([1, 0, 1, 0])  # Mensaje de 4 bits
encoded_message = hamming_encode(message)
print("Mensaje codificado:", encoded_message)
