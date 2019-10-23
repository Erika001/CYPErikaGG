SUMPAR = 0
SUMIMP = 0
CUEPAR = 0
CONT = 0
for i in range(1,271,1):
    NUM = int(input("Ingrese un numero entero: "))
    if NUM  > 0:
        if (-1 ** NUM) > 0:
            SUMPAR += NUM
            CUEPAR += 1
        else:
            SUMIMP += NUM
    elif NUM < 0:
        if (-1 ** NUM) > 0:
            SUMPAR += NUM
            CUEPAR += 1
        else:
            SUMIMP += NUM

PROPAR = SUMPAR / CUEPAR
CONT += 1
    
print(f"El promedio de los numeros pares es: {PROPAR}, y la suma de estos numeros es: {SUMIMP}")
