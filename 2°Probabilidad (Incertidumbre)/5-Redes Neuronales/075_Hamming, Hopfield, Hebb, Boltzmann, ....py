# Importando la librería numpy para manipulación de matrices y cálculos matemáticos
import numpy as np

# Función para calcular la paridad utilizando el código de Hamming
def hamming_encode(bits):
    """
    Codifica un mensaje de 4 bits con el código de Hamming de 7 bits
    La matriz de paridad G se utiliza para generar la codificación de 7 bits
    a partir de un mensaje de 4 bits.
    """
    # Generar la matriz de paridad G (matriz generadora de Hamming)
    # Esta matriz tiene 7 filas y 4 columnas, que representa la codificación de 4 bits a 7 bits
    G = np.array([[1, 1, 0, 1], 
                  [1, 0, 1, 1], 
                  [1, 0, 0, 0], 
                  [0, 1, 1, 1], 
                  [0, 1, 0, 0], 
                  [0, 0, 1, 0], 
                  [0, 0, 0, 1]])
    
    # Codificación del mensaje de 4 bits a 7 bits
    # Realiza una multiplicación matricial entre el mensaje de entrada y la matriz G
    # El resultado se realiza módulo 2 (operación XOR) para obtener la paridad
    return np.dot(bits, G) % 2

# Ejemplo de uso de la función de codificación de Hamming
# El mensaje de 4 bits que se desea codificar
message = np.array([1, 0, 1, 0])  # Mensaje de 4 bits
# Codificación del mensaje
encoded_message = hamming_encode(message)
# Mostrar el mensaje codificado
print("Mensaje codificado:", encoded_message)
