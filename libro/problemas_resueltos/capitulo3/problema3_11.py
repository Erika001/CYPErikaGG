CAN1 = 0
CAN2 = 0
CAN3 = 0
CAN4 = 0
CAN = 0
VOTO = int(input("Determine el voto para un CAN del 1-4: "))
while(VOTO != 0):
    if VOTO == 1:
       CAN1 + 1
    elif VOTO == 2:
         CAN2 + 1
    elif VOTO == 3:
         CAN3 + 1
    elif VOTO == 4:
         CAN4 + 1
    else:
        print("Valor invalido")
    VOTO = int(input("Determine el voto para un CAN del 1-4: "))
SUMV = CAN1 + CAN2 + CAN3 + CAN4
POR1 = (CAN1 / SUMV) *100
POR2 = (CAN2 / SUMV) *100
POR3 = (CAN3 / SUMV) *100
POR4 = (CAN4 / SUMV) *100
print(f"Votos candidato 1: {CAN1}, el porcentaje: {POR1}")
print(f"Votos candidato 2: {CAN2}, el porcentaje: {POR2}")
print(f"Votos candidato 3: {CAN3}, el porcentaje: {POR3}")
print(f"Votos candidato 4: {CAN4}, el porcentaje: {POR4}")
print(f"Las cantidades votantes son: {SUMV}")
print("Fin del programa")


