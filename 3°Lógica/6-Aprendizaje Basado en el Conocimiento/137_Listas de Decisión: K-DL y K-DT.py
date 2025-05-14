# Implementación simple de K-DL (Listas de Decisión) y K-DT (Árboles de Decisión)

def k_dl(datos, k):
    # Función simple de K-DL: selecciona los primeros 'k' elementos como hipótesis
    return datos[:k]  # Devuelve los primeros 'k' elementos de la lista de datos

def k_dt(datos, k):
    # Función simple de K-DT: devuelve el valor de la 'k'-ésima fila
    return datos[k]  # Devuelve el valor en la posición 'k' (índice 'k' de la lista)

# Datos de ejemplo
datos = [1, 2, 3, 4, 5]  # Lista de datos a analizar

# Ejecución de las funciones con 'k' específicos
print("K-DL (primeros 3):", k_dl(datos, 3))  # Muestra los primeros 3 elementos de la lista
print("K-DT (valor en la posición 2):", k_dt(datos, 2))  # Muestra el valor en la posición 2 (índice 2)
