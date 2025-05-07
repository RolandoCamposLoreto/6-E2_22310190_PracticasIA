# Lógica modal simulada

def necesario(hecho):
    return hecho == True

def posible(hecho):
    return hecho in [True, False]

print("¿Es necesario que 2 + 2 = 4?:", necesario(2 + 2 == 4))
print("¿Es posible que 2 + 2 = 5?:", posible(2 + 2 == 5))
