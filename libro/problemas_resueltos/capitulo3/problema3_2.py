SUMSER = 0
BAND = 'T'
i = 2
while(i <= 1800):
    SUMSER += i
    print(i)
    if BAND == 'T':
       BAND = 'F'
       i += 3
    else:
       BAND = 'T'
       i += 2
else:
    print(f"Los terminos de la serie son: {SUMSER}")
print("Fin del programa")



