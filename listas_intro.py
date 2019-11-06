lista = []
lista2 = list()

print(lista)
print(lista2)

numeros = [2,3,6,2,7,34,13,0]
print(numeros)
print(numeros[2])
print(numeros[-1])

# slicing
print(numeros[2:4:1])
print(numeros[2:7:])
print(numeros[:-4:-1])

cosas = ["Jose", 22, 1.67, True, None, [3,4,2,5,2]]
print(cosas)
print(cosas[3])
print(cosas[5])
print(cosas[5][2])
cosas[1]=33
print(cosas)
cosas[3]=False
print(cosas)

# string por separado split
fecha='12/05/2019'
lista_fecha = fecha.split('/')
print(lista_fecha)

crudos = "  34  , 45 , 55, 53 , 89 , 43 ,3 ,2 , 1 , 6 "
print(crudos)
lista_numeros = crudos.split(',')
print(lista_numeros)
print(lista_numeros[0])

# strip quita espacios
lista_numeros[0] = lista_numeros[0].strip()
print(lista_numeros)

#index vuelve enteros
for index in range(len(lista_numeros)):
    lista_numeros[index] = int(lista_numeros[index].strip())
print(lista_numeros)

# .sort pone los valores en orden
lista_numeros.sort()
print(lista_numeros)
lista_numeros.reverse()
print(lista_numeros)
lista_numeros.append(0)
print(lista_numeros)
lista_numeros.append(455)
lista_numeros.append(100)
lista_numeros.append(200)
lista_numeros.sort()
print(lista_numeros)

dias_semana=["Lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
print(';'.join(dias_semana))
cadena_dias=';'.join(dias_semana)
print(cadena_dias)

# .remove para remover o borrar
frutas = ['fresa','kiwi','platano','aguacate','piña']
print(frutas)
frutas.remove('piña')
print(frutas)
# .append para agregar
frutas.append('naranja')
print(frutas)
# .insert para agregar otro valor entre unos
frutas.insert(1,'sandia')
print(frutas)
# .index que posicion tiene un valor esp
print(frutas.index('kiwi'))
# .extend le agrega a una lista otra al final
otras_frutas = ['melon','papaya','limon']
frutas.extend(otras_frutas)
print(frutas)
