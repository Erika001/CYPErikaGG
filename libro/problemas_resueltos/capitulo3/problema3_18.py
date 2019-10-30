MAYPRO = 0
N = int(input("Determine el numero de fabricas registradas: "))
if N <= 1000:
    I = 1
    for I in range(I,N,1):
        FABRICA = int(input("Indique la clave de la fabrica: "))
        TOTANU = 0
        J = 1
        for J in range(J,13,1):
            MES = float(input("Determine la produccion de la fabrica: "))
            TOTANU += MES
            if J == 7 and MES >3000000:
                print(FABRICA)
                J += 1
        if TOTANU > MAYPRO:
            MAYPRO = TOTANU
            CLAVE = FABRICA
            print(f"Produccion anual fabrica: {FABRICA}, :$ {TOTANU}")
            I += 1
    print(f"Fabrica que mas produjo en el año: {CLAVE}, produccion: ${MAYPRO}")
else:
    print("Error en numero de fabricas")
print("Fin del programa")


