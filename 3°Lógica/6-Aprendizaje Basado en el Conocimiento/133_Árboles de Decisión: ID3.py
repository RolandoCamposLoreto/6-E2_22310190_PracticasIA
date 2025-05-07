# Implementación simple del algoritmo ID3 para árboles de decisión
import math

def calcular_entropia(datos):
    total = len(datos)
    positivos = sum([1 for d in datos if d == 1])
    negativos = total - positivos
    if positivos == 0 or negativos == 0:
        return 0
    p_pos = positivos / total
    p_neg = negativos / total
    return - (p_pos * math.log2(p_pos) + p_neg * math.log2(p_neg))

def id3(datos, atributos, objetivo):
    if len(set([dato[objetivo] for dato in datos])) == 1:
        return datos[0][objetivo]  # Si todos son iguales, se devuelve el valor
    if not atributos:
        return max(set([dato[objetivo] for dato in datos]), key=[dato[objetivo] for dato in datos].count)

    mejor_atributo = None
    mejor_entropia = float("inf")
    for atributo in atributos:
        valores = set([dato[atributo] for dato in datos])
        entropia_total = 0
        for valor in valores:
            subset = [dato for dato in datos if dato[atributo] == valor]
            entropia_total += len(subset) / len(datos) * calcular_entropia([dato[objetivo] for dato in subset])
        if entropia_total < mejor_entropia:
            mejor_entropo = entropia_total
            mejor_atributo = atributo

    return mejor_atributo

# Datos de ejemplo
datos = [
    {"color": "rojo", "tamano": "grande", "compra": 1},
    {"color": "rojo", "tamano": "pequeno", "compra": 0},
    {"color": "verde", "tamano": "grande", "compra": 1},
    {"color": "verde", "tamano": "pequeno", "compra": 0},
]
atributos = ["color", "tamano"]
objetivo = "compra"

print("Mejor Atributo para dividir:", id3(datos, atributos, objetivo))
