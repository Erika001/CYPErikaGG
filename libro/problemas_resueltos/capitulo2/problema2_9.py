PREBAS = float(input("Precio basico del producto: "))
IMP = 0
PRETOT =0
if PREBAS > 500:
    IMP = (20*0.30+(PREBAS - 40)*0.50)
elif PREBAS > 40:
    IMP = (20*0.30+(PREBAS - 40)*0.40)
elif PREBAS > 20:
    IMP = ((PREBAS-20)*0.30)
else:
    IMP = 0
PRETOT = PREBAS + IMP
print(f"El precio basico del producto es: {PREBAS}$, su precio total es: {PRETOT}$")
print(f"El impuesto del producto es: {IMP}")
print("Fin del programa")


