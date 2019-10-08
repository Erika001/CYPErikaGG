CATE = int(input("Determine la categoria del empleado (1-4): "))
SUE = float(input("Determine el sueldo del empleado; "))
NSUE = 0
if CATE == 1:
    NSUE = SUE * 1.15
elif CATE == 2:
    NSUE = SUE * 1.10
elif CATE == 3:
    NSUE = SUE * 1.08
elif CATE == 4:
    NSUE = SUE * 1.07
print(f"La categoria de el empleado es {CATE}, y el su nuevo sueldo es de: {NSUE}")
print("Fin del programa!!")



