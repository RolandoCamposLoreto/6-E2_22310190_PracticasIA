# Sin necesidad de librerías externas para este ejemplo

# Probabilidades
p_lluvia = 0.3       # 30% probabilidad de que llueva
p_no_lluvia = 0.7    # 70% probabilidad de que no llueva

# Utilidades sin información (sin saber el clima)
# Decisión: Ir o No ir
# Si vas y llueve → -10 (te mojas), si vas y no llueve → +10 (lo disfrutas)
# Si no vas en ambos casos → 0
util_ir = p_lluvia * (-10) + p_no_lluvia * 10
util_no_ir = 0

print("🔸 Utilidad esperada sin información:")
print(f"Ir al parque: {util_ir}")
print(f"No ir: {util_no_ir}")
print(f"Mejor decisión sin información: {'Ir' if util_ir > util_no_ir else 'No ir'}")

# Ahora supongamos que tienes información perfecta (sabes si lloverá o no)
# Calculamos la utilidad esperada con información perfecta

# Si sabes que lloverá, eliges no ir: utilidad = 0
# Si sabes que no lloverá, eliges ir: utilidad = 10
util_con_info = p_lluvia * 0 + p_no_lluvia * 10

print("\n🔸 Utilidad esperada con información perfecta:")
print(f"{util_con_info}")

# Valor de la información perfecta = utilidad con info - utilidad sin info
voi = util_con_info - max(util_ir, util_no_ir)
print("\n🔸 Valor de la información perfecta (VOI):")
print(f"{voi}")
