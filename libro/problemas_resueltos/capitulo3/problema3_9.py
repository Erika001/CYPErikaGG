SERIE = 0
N = int(input("Determine los terminos de la serie: "))
i = 1
for i in range(i,N,1):
    SERIE += i ** i
    i + 1
print(f"La serie es {SERIE}")

