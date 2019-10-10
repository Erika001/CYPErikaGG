A = int(input("Introduzca un entero positivo: ")) 
B = int(input("Introduzca otro entero positivo: "))
C = int(input("Introduzca otro entero positivo: "))
if A > B:
    if A > C:
        print(f"A es el mayor con valor a {Á}")
    elif A == C:
        print(f"A y C son iguales a  {A} y son los mayores")
    else:
        print(f"C que vale {C} es el mayor")
elif A == B:
    if A > C:
        print(f"A y B son los mayores con valor {B} ")
    elif A == C:
        print(f"Los tres son iguales a {B}")
    else:
        print(f"C que vale {c} es el mayor")
elif B > C:
    print(f"B que vale {B} es el mayor")
elif B == C:
    print(f"B Y C son los mayores con valor {B}")
else:
    print(f"C es el mayor con valor {C}")
print("Fin del programa")

