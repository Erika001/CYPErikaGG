A = int(input("Ingrese una primer variable de tipo entero: ")) 
B = int(input("Ingrese una segunda variable de tipo entero: "))
C = int(input("Ingrese una tercera variable de tipo entero: "))
if A < B:
    if B < C:
        print("Los numeros estan en orden creciente")
    else:
        print("Los numeros no estan en orden creciente")
else:
    print("Los numeros no estan en orden creciente")
print("Fin del programa")

