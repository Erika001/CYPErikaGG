ARSU = 0
ARNO = 0
MERSU = 50000
ARCE = 0
MES = 0
for i in range(1, 13 ,1):
    print(f" Mes (i): ")
    RNO = int(input("Promedio de lluvias del mes zona norte: "))
    RCE = int(input("Promedio de lluvias del mes zona centro: "))
    RSU = int(input("Promedio de lluvias del mes zona sur: "))

    ARNO = ARNO + RNO
    ARCE = ARCE + RCE
    ARSU = ARSU + RSU

    if RSU < MERSU:
        MERSU = RSU
        MES = i
PRORCE = ARCE / 12
print(f"Promedio region centro: {PROCE} ")
print(f"Mes con menor lluvia en reg. sur: {MES}")
print(f"Registro con menor lluvia es:{MERSU}")

if ARNO > ARCE:
    if ARNO > ARSU:
        print("La region con mayor lluvia es norte")
    else:
        print("La region con mayor lluvia es sur")
elif ARCE > ARSU:
    print("La region con mayor lluvia es centro")
else:
    print("La region con mayor lluvia es sur")
print("fin del programa")
