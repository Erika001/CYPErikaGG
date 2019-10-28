MASUE = 0 
N = int(input("Determine el numero de empleados: "))
i = 1
for i in range(i,N,1):
    NUMEMP = int(input("Determine el numero del empleado: "))
    SUE = int(input("Determine el sueldo del empleado: "))
    if SUE > MASUE:
        MASUE = SUE 
        MANUM = NUMEMP
    i = i + 1
print(f"El empleado con mayor sueldo es: {MANUM}, el mayor sueldo es: {MASUE}")
print("Fin del programa")
