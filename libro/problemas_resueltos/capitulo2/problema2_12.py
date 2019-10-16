SUE = float(input("Determine su sueldo: "))
CATE = int(input("Determine su categoria: "))
HE = int(input("Ingrese las horas extras trabajadas: "))
PHE = 0
NSUE = 0
if CATE == 1:
    PHE = 30
elif CATE == 2:
    PHE = 38
elif CATE == 3:
    PHE = 50
elif CATE == 4:
    PHE = 70
elif CATE > 4:
    PHE = 0
if HE > 30:
    NSUE = SUE + 30 * PHE
else:
    NSUE = SUE + HE * PHE
print(f"El precio por sus horas extras {PHE}$ y de su nuevo sueldo es de: {NSUE}$")
print("Fin del programa")
 

