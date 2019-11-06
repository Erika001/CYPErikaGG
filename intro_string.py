nombre = "Jose sosa"
print(nombre)
print(nombre[0])
print(nombre[8])

# indexado positivo y negativo
print(nombre[-1])
print(nombre[-4])

# Slicing
print(nombre[1:3:1])

# Valores por defecto
print(nombre[5::1])
print(nombre[::])
print(nombre[0:4:2])

# slicing negativo
print(nombre[-1:-5:-1])
print(nombre[::-1])
print(nombre[-6:-10:-1])

frase = "Solo existen 10 tipos de personas,las que saben binario y las que no"
# hacer in clicing para imprimir la palabra existen
print(frase[5:12:1])
# imprimit la palabra personas en orden inverso
print(frase[-36:-44:-1])
# slicing que imprima toda la frase en orden inverso
print(frase[::-1])

print(dir(nombre))
print("Funciones de string (str)")
# upper las vuelve mayusculas
print(nombre.upper())
print(f"la palabra 'existen' esta en la pos. {frase.find('existen') }")

