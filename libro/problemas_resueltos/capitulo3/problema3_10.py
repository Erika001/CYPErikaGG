PRI = 0
SEG = 1
i = 3
for i in range(i,181,1):
    SIG = PRI + SEG
    PRI = SEG 
    SEG = SIG
    i = i + 1
print(f"El siguente numero de la serie es {SIG}")


