TIPOENF = int(input("Determine el tipo de enfermedad del (1-4): "))
EDAD = int(input("Ingrese edad: "))
DIAS = int(input("Ingrese los dias de estancia: "))
COSTOT = 0
if TIPOENF == 1:
    COSTOT = DIAS * 25
elif TIPOENF == 2:
    COSTOT = DIAS * 16
elif TIPOENF == 3:
    COSTOT = DIAS * 20
elif TIPOENF == 4:
    COSTOT = DIAS * 32
if EDAD >= 14:
    if EDAD <= 22:
        COSTOT = COSTOT * 1.10
    else:
        print("El costo total es: " ,COSTOT)
print("Fin del programa")

