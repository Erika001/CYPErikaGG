N = int(input("Determine el limite de los numeros: "))
I = 1
for I in range(I,N,1):
    SUM = 0
    J = 1
    for J in range(J,(1/2),1):
        if (I MOD J)== 0:
            SUM += J
        J += 1
    if SUM == 1:
        print(f"{I}, es un numero perfecto")
    I += 1
print("Fin del programa")

