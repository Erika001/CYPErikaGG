MAT = int(input("Ingrese la matricula del alumno: "))
CAL1 = float(input("Ingrese la primera calificacion: "))
CAL2 = float(input("Ingrese la segunda calificacion: "))
CAL3 = float(input("Ingrese la tercera calificacion: "))
CAL4 = float(input("Ingrese la cuarta calificacion: ")) 
CAL5 = float(input("Ingrese la quinta calificacion: "))
PRO = (CAL1 + CAL2 + CAL3 + CAL4 + CAL5)/5
if PRO >= 6:
     print(f"La matricula {MAT} tiene de promedio {PRO}, Aprobado")
else:
     print(f"La matricula {MAT} tiene de promedio {PRO}, NO APROBADO")
print("Fin del programa")  

