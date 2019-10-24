MAY = -100000
MEN = 100000
N = int(input("Numeros enteros a ingresar?: "))
i = 1
for i in range(i,N,1):
    NUM = int(input("Ingrese el valor: "))
    if NUM > MAY :
        MAY = NUM
    elif NUM < MEN:
        MEN = NUM
    i + 1
print(f"El valor mayor es: {MAY} y menor es: {MEN}")

