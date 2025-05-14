import math  # Importar la librería 'math' para usar logaritmos y funciones matemáticas

# Función para calcular la entropía de un conjunto de datos
def calcular_entropia(datos):
    total = len(datos)  # Contar el total de datos en el conjunto
    positivos = sum([1 for d in datos if d == 1])  # Contar cuántos de los datos son positivos (1)
    negativos = total - positivos  # El resto son negativos (0)

    # Si todos los datos son positivos o negativos, la entropía es 0
    if positivos == 0 or negativos == 0:
        return 0  

    # Calcular la probabilidad de los datos positivos y negativos
    p_pos = positivos / total  # Probabilidad de positivos
    p_neg = negativos / total  # Probabilidad de negativos

    # Calcular la entropía utilizando la fórmula de Shannon
    return - (p_pos * math.log2(p_pos) + p_neg * math.log2(p_neg))

# Algoritmo ID3 para encontrar el mejor atributo para dividir el conjunto de datos
def id3(datos, atributos, objetivo):
    # Si todos los ejemplos tienen el mismo valor para el objetivo, devolver ese valor
    if len(set([dato[objetivo] for dato in datos])) == 1:
        return datos[0][objetivo]  # Todos los valores de la columna 'objetivo' son iguales, se devuelve ese valor
    
    # Si no hay más atributos para dividir, devolver el valor más frecuente del objetivo
    if not atributos:
        # Encontrar el valor más frecuente de la columna 'objetivo'
        return max(set([dato[objetivo] for dato in datos]), key=[dato[objetivo] for dato in datos].count)

    mejor_atributo = None  # Inicializar el mejor atributo como 'None'
    mejor_entropia = float("inf")  # Inicializar la mejor entropía con el valor más alto posible

    # Recorrer cada atributo para calcular su entropía
    for atributo in atributos:
        # Obtener los valores únicos de este atributo en el conjunto de datos
        valores = set([dato[atributo] for dato in datos])
        
        entropia_total = 0  # Inicializar la entropía total para este atributo
        
        # Calcular la entropía total para este atributo considerando sus diferentes valores
        for valor in valores:
            # Crear un subconjunto de datos donde el atributo tiene el valor actual
            subset = [dato for dato in datos if dato[atributo] == valor]
            
            # Calcular la entropía de este subconjunto y agregarla al total ponderado
            entropia_total += len(subset) / len(datos) * calcular_entropia([dato[objetivo] for dato in subset])
        
        # Si la entropía total para este atributo es menor que la mejor entropía, actualizar
        if entropia_total < mejor_entropia:
            mejor_entropia = entropia_total  # Actualizar la mejor entropía
            mejor_atributo = atributo  # Actualizar el mejor atributo

    return mejor_atributo  # Devolver el atributo con la menor entropía

# Datos de ejemplo (conjunto de datos)
datos = [
    {"color": "rojo", "tamano": "grande", "compra": 1},  # Ejemplo donde se compró (compra = 1)
    {"color": "rojo", "tamano": "pequeno", "compra": 0},  # Ejemplo donde no se compró (compra = 0)
    {"color": "verde", "tamano": "grande", "compra": 1},  # Ejemplo donde se compró (compra = 1)
    {"color": "verde", "tamano": "pequeno", "compra": 0},  # Ejemplo donde no se compró (compra = 0)
]

atributos = ["color", "tamano"]  # Atributos disponibles para dividir
objetivo = "compra"  # El objetivo es predecir si se compró o no (compra)

# Imprimir el mejor atributo para dividir según el algoritmo ID3
print("Mejor Atributo para dividir:", id3(datos, atributos, objetivo))
