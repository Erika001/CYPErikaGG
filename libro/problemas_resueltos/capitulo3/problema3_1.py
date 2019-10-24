SUMPAR = 0
SUMIMP = 0
CUEPAR = 0
for i in range(1,271,1):
    NUM = int(input("Ingrese un numero entero: "))
    if NUM  != 0:
        if (-1) ** NUM > 0:
            SUMPAR += NUM
            CUEPAR += 1
        else:
            SUMIMP += NUM
else:
    PROPAR = SUMPAR / CUEPAR
    print(f"El promedio de los numeros pares es: {PROPAR}, y la suma de estos numeros es: {SUMIMP}")
print("Findel programa")

