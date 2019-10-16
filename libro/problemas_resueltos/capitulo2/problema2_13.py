MAT = int(input("Ingrese matricula: "))
CARR = str(input("Determine carrera: "))
SEM = int(input("Ingrese semestre: "))
PROM = float(input("Ingrese promedio: "))
economia = 0
computacion = 0
contabilidad = 0
administracion = 0
if CARR == 'economia':
    if SEM >= 6:
        if PROM >= 8.8:
            print(f"La matricula {MAT}, esta aceptado en economia!")
        else:
          print("Alumno rechazado")
elif CARR == 'computacion':
    if SEM > 6:
        if PROM > 8.5:
            print(f"La matricula {MAT}, esta aceptado en computacion!")
        else:
            print("Alumno rechazado")
elif CARR == 'contabilidad': 
    if SEM > 5:
        if PROM > 8.5:
            print(f"La matricula {MAT}, esta aceptado en {CARR}")
        else:
            print("Alumno rechazado")
elif CARR == 'economia':
    if SEM > 5: 
        if PROM > 8.5:
            print(f"La matricula {MAT}, esta aceptado en {CARR}")
        else:
            print("Alumno rechazado")
elif CARR == 'administracion':
    if SEM > 5:
        if PROM > 8.5:
            print(f"La matricula {MAT}, esta aceptado en {CARR}")
        else:
            print("Alumno rechazado")

print("Fin del programa")

