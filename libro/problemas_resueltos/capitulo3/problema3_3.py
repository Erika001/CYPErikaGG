SERIE = 0
N = int(input("Determine los terminos de la serie: "))
BAND = 'T'
i = 1
for i in range(i, N, 1):
    if BAND == 'T':
        SERIE = SERIE + 1 / i
        BAND ='F'
    else:
        SERIE = SERIE - 1 / i
        BAND = 'T'
    i = i+1
else:
    print(f"El resultado de la serie es {SERIE}")
print("Fin del programa")


