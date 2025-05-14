# Probabilidades
p_lluvia = 0.3       # 30% probabilidad de que llueva
p_no_lluvia = 0.7    # 70% probabilidad de que no llueva

# Utilidades sin información (sin saber el clima)
# Decisión: Ir o No ir
# Si vas y llueve → -10 (te mojas), si vas y no llueve → +10 (lo disfrutas)
# Si no vas en ambos casos → 0
util_ir = p_lluvia * (-10) + p_no_lluvia * 10
# La utilidad de ir es la suma de los valores ponderados por las probabilidades: 
# 30% de que llueva y te mojes (-10) + 70% de que no llueva y disfrutes (+10)
util_no_ir = 0  # La utilidad de no ir es 0 porque no te mojas ni disfrutas nada

print("🔸 Utilidad esperada sin información:")
print(f"Ir al parque: {util_ir}")  # Imprime la utilidad esperada si decides ir
print(f"No ir: {util_no_ir}")  # Imprime la utilidad esperada si decides no ir
print(f"Mejor decisión sin información: {'Ir' if util_ir > util_no_ir else 'No ir'}")
# Compara las utilidades para elegir la mejor opción sin información perfecta

# Ahora supongamos que tienes información perfecta (sabes si lloverá o no)
# Calculamos la utilidad esperada con información perfecta

# Si sabes que lloverá, eliges no ir: utilidad = 0
# Si sabes que no lloverá, eliges ir: utilidad = 10
util_con_info = p_lluvia * 0 + p_no_lluvia * 10
# La utilidad esperada con información perfecta es 0 si llueve (porque no vas)
# y 10 si no llueve (porque decides ir al parque y disfrutar)

print("\n🔸 Utilidad esperada con información perfecta:")
print(f"{util_con_info}")  # Imprime la utilidad esperada con información perfecta

# Valor de la información perfecta = utilidad con info - utilidad sin info
voi = util_con_info - max(util_ir, util_no_ir)
# Calcula el valor de la información perfecta como la diferencia entre la utilidad 
# con información perfecta y la mayor utilidad sin información

print("\n🔸 Valor de la información perfecta (VOI):")
print(f"{voi}")  # Imprime el valor de la información perfecta (VOI)
