# print tiene 4 formas de uso
"""
1.- con comas
2.- con signo '+'
3.- con la funcion format ()
4.- es con una variante de format()
"""
# Con comas, concatenar agregando un espacio y haciendo casting de tipo
edad = 10
nombre = "Juan"
estatura = 1.67
print(edad, nombre, estatura)

# con '+' hace lo mismo pero no realiza el casting automatico no agrega espacio
print(str(edad) + str(estatura) + nombre)

# funcion format()

print("Nombre: {} Edad: {} ".format(nombre, edad))
      
#4.- es con una variante de format () simplificada

print(f"Nombre: \"{nombre}\" \nEdad:\t{edad} ")

# print y el argumento end
print("solo hay dos tipos de personas, las que saben binario y las que no")
print("otra linea")
