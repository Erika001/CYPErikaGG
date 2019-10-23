SUMSER = 0
BAND = 'T'
i = 2
for i in range(i, 1801, ):
    SUMSER += i
    print(i)
if BAND == 'T':
    BAND = 'F'
    i += 3
else:
    BAND = 'T'
    i += 2
print(f"Los terminos de la serie son: {SUMSER}")


