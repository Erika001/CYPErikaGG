AP1 = 0
AP2 = 0
AP3 = 0
AP4 = 0
AP5 = 0
RECAU = 0
P1 = float(input("Determine el primer precio: "))
P2 = float(input("Determine el segundo precio: "))
P3 = float(input("Determine el tercer precio: "))
P4 = float(input("Determine el cuarto precio: "))
P5 = float(input("Determine el quinto precio: "))
CLAVE = int(input("Ingrese la clave de la localidad del al 1-5: "))
CANT = int(input("Determine cuantos boletos: "))
while(CLAVE != -1 and CANT != -1):
    if CLAVE == 1:
        PRE = P1 * CANT 
        AP1 += CANT
    elif CLAVE == 2:
        PRE = P2 * CANT 
        AP2 += CANT
    elif CLAVE == 3:
        PRE = P3 * CANT
        AP3 += CANT
    elif CLAVE == 4:
        PRE = P4 * CANT
        AP4 += CANT
    elif CLAVE == 5:
        PRE = P5 * CANT
        AP5 += CANT
    else:
        print("Opcion no valida")
    print(f"La clave es {CLAVE}, la cantidad de boletos {CANT} y total vendido {PRE}")
    RECAU += PRE
    CLAVE = int(input("Ingrese la clave de la localidad del al 1-5: "))
    CANT = int(input("Determine cuantos boletos: "))
print(f"Cantidad de boletos tipo 1: {AP1}")
print(f"Cantidad de boletos tipo 2: {AP2}")
print(f"Cantidad de boletos tipo 3: {AP3}")
print(f"Cantidad de boletos tipo 4: {AP4}")
print(f"Cantidad de boletos tipo 5: {AP5}")
print(f"Recaudacion del estadio: {RECAU}")
print("Fin del programa")


    
