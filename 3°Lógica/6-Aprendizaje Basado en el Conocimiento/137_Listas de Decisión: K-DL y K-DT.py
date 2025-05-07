# Implementación simple de K-DL (Listas de Decisión) y K-DT (Árboles de Decisión)
def k_dl(datos, k):
    # Función simple de K-DL: selecciona los primeros 'k' elementos como hipótesis
    return datos[:k]

def k_dt(datos, k):
    # Función simple de K-DT: devuelve el valor de la 'k'-ésima fila
    return datos[k]

# Datos de ejemplo
datos = [1, 2, 3, 4, 5]

print("K-DL (primeros 3):", k_dl(datos, 3))
print("K-DT (valor en la posición 2):", k_dt(datos, 2))
