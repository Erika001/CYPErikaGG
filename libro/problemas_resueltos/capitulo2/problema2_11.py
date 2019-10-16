CLAVE = int(input("Determine a que zona geografica llamara: "))
NUMIN = int(input("Determine los minutos de su llamada: "))
COST = 0
if CLAVE == 12:
    COST = NUMIN*2
elif CLAVE == 15:
     COST = NUMIN*2.2
elif CLAVE == 18: 
     COST = NUMIN*4.5
elif CLAVE == 19: 
     COST = NUMIN*3.5
elif CLAVE == 23:
     COST = NUMIN*6
elif CLAVE == 25: 
     COST = NUMIN*6
else: 
    CLAVE == 29 
    COST = NUMIN*5
print(f"El costo de su llamada ha sido de: {COST}")
print("Fin del programa")

