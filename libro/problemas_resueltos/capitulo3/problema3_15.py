CL = 0
CUENTA = 0
TIPO = str(input("Determine el tipo de su llamada con I,N y L: "))
DUR = int(input("Determine los minutos de su llamada: "))
while(TIPO != 'X' and DUR != -1):
    if TIPO == 'I':
        if DUR > 3:
            COSTO = 7.59 + (DUR - 3) * 3.03
        else:
            COSTO = 7.59
    elif TIPO == 'L':
        CL = CL + 1
        if CL > 50 :
            COSTO = 0.60
        else:
            COSTO = 0
    elif TIPO == 'N':
        if DUR > 3:
            COSTO = 1.20 + ((DUR-3) * 0.48)
        else:
            COSTO = 1.20
    else:
        print("Opcion invalida")
    CUENTA += COSTO
    TIPO = str(input("Determine el tipo de su llamada con I,N y L: "))
    DUR = int(input("Determine los minutos de su llamada: "))
print(f"Su cuenta es de: {CUENTA}")
print("Fin del programa")

