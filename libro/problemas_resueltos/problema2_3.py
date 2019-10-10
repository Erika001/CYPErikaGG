A = float(input("Introduzca el valor de a: "))
B = float(input("Introduzca el valor de b: "))
C = float(input("Introduzca el valor de c: "))
DIS = B ** 2 - 4 * A * C
if DIS >= 0:
    X1 = ((-B)+DIS**0.5)/2*A
    X2 = ((-B)-DIS**0.5)/2*)
    print(f"Las raices de la ecuacion son; X1: {X1} y X2: {X2}")
     
print("Valores no encontrados")
print("Fin del programa")


