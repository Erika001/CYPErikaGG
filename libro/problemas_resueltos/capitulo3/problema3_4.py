NOM = 0
T = int(input("Determine cuantos trabajadores: "))
SUE = float(input("Ingrese el sueldo del trabajador:"))
for SUE in range(0, T ,1):
    if SUE < 1000:
        NSUE = SUE * 1.15
    else:
        NSUE = SUE * 1.12
    NOM += NSUE
    print(f"El nuevo sueldo es de: {NSUE}")
SUE = float(input("Ingrese el sueldo del trabajador:"))
print("El los nuevos sueldos de los trabajadores son: {NOM}")


