COMPRA = float(input("De cuanto es el momnto de su compra?: "))
if COMPRA < 500:
    print(f"Su compra es de {COMPRA}, por lo tanto no aplica descuento")
elif COMPRA <= 1000:
    print(f"Su compra fue de {COMPRA}, y con el descuento pagara: {COMPRA - COMPRA * 0.05}$")
elif COMPRA <= 7000:
    print(f"Su compra fue de {COMPRA}, y con el descuento pagara: {COMPRA - COMPRA * 0.11}$")
elif COMPRA <= 15000:
    print(f"Su compra fue de {COMPRA}, y con el descuento pagara: {COMPRA - COMPRA * 0.18}$")   
else:
    print(f"Su compra fue de {COMPRA}, y con el descuento pagara: {COMPRA - COMPRA* 0.25}$")
print("Fin del programa")





