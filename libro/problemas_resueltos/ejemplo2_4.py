SUE = float(input("Ingrese su sueldo: "))
if SUE < 1000 :
   AUM = SUE * 1.15
   print(f"Su nuevo sueldo con el aumento del 15% es de: ${AUM}") 
else:
   AUM = SUE * 1.12
   print(f"Su nuevo sueldo con el aumento del 12% es de: ${AUM} ")


