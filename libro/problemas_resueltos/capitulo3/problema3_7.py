MED = 0
CHI = 0
GRA = 0
N = int(input("Determine el numero de ventas: "))
i = 1
for i in range(i,N,1):
    V = float(input("Ingrese la venta: "))
    if V <= 200:
        CHI += 1
        if V < 400:
             MED += 1
        else:
            GRA += 1
    i + 1
print(f"La venta menor es: {CHI}, la mediana {MED} y la grande es {GRA}")
    
