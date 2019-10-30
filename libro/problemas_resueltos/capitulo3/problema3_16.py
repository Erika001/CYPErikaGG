TIPO1 = 0
TIPO2 = 0
TIPO3 = 0
TIPO4 = 0
TIPO5 = 0
MCTIPO2= 0
N = int(input("Ingrese los años en los que desea su informacion: "))
I = 0
for I in range(I,N,1):
    J = 1
    TOTVIN = 0
    for J in range(J,5,1):
        V = float(input("Determine los litros de vino durante estos años: "))
        TOTVIN += V
        if J == 1:
            TIPO1 = TIPO1 + V
        elif J == 2:
            TIPO2 = TIPO2 + V
            if V > MCTIPO2:
                MCTIPO2 = V
                AÑO =  I
        elif J == 3:
            TIPO3 = TIPO3 + V
            if V == 0:
                print(f"En el año: {I}, no se produjo vino TIPO3")
        elif J == 4:
            TIPO4 = TIPO4 + V
        elif J == 5:
            TIPO5 = TIPO5 + V
        else:
            print("Opcion no valida")
        J += 1
    print(f"Total de litros producidos por año: {TOTVIN}")
    I += 1
print(f"Total TIPO1: {TIPO1}")
print(f"Total TIPO2: {TIPO2}")
print(f"Total TIPO3: {TIPO3}")
print(f"Total TIPO4: {TIPO4}")
print(f"Total TIPO5: {TIPO5}")
print(f"Año en el que se produjo mayor cantidad de vino TIPO2: {AÑO}, litros: {MCTIPO2}")
print("Fin del programa")

