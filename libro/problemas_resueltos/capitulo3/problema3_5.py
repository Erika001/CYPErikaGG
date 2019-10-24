SUMOTR = 0
SUMPOS = 0
CUEPOS = 0
N = int(input("Determine los datos a ingresar: "))
i = 0
for i in range(i,N,1):
    NUM = int(input("Ingrese un numero entero: "))
    if NUM > 0:
        SUMPOS += NUM
        CUEPOS += 1
    else:
        SUMOTR += NUM
    i + 1
PROGEN = (SUMPOS + SUMOTR)/N
PROPOS = SUMPOS/CUEPOS
print(f"Los numeros positivos son: {CUEPOS}, y el promedio de estos son: {PROPOS}.y el promedio grl. es de: {PROGEN}")








