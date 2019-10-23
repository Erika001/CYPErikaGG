SERIE = 0
N = int(input("Determine los terminos de la serie: "))
BAND = 'T'
I = 1
for I in range(0, N, I):
    if BAND == 'T':
        SERIE = N + 1 / I
        BAND ='F'
    else:
        SERIE = N - 1 / I
        BAND = 'T'
    I = I + 1
print(SERIE)
print("Fin del programa")


