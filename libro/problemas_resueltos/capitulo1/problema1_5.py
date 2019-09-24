RADIO = float(input(“Determine el radio del cilindro”))
ALTU = float(input(“Determine la altura del cilindro”))
VOL = 3.141592 * (RADIO ** 2) * ALTU
ARE = 2 * 3.141592 * RADIO * ALTU
print(f”El volumen del cilindro = π * (radio)**2 * altura, es: {VOL}”)
print(f”La superficie de el cilindro = 2 * π * radio * altura, es de: {ARE})

