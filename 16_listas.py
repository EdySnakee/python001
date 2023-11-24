#> LAS LISTAS NOS PERMITEN ALMACENAR VARIOS TIPOS DE DATOS

#-> NUMBER
num = [1,2,3,4,5,6]
print(num)
print(type(num))

#-> STRING 
saludos = ['hi','hola', 'huevos']
print(saludos) 

#-> VARIOS TIPOS DE DATOS
tipos = [1, True, 'hola']
print(tipos)

#-> index
print(num[0]) #-> VAMOS A LA POSICION 0 DE LA LISTA = 1 
print(saludos[2]) #-> VAMOS A LA POSICION 0 DE LA LISTA = huevos

#-> MUTACIONES
#-> se pueden mutar cuantas veces sea necesario
saludos[0] = 'nhe'
print(saludos)
saludos[0] = 'otra'
print(saludos)

#-> seleccionar numeros de la lista
print(num[:3]) #= [1, 2, 3]

#-> in types,podemos confirmar o negar la existencia
print( True in tipos) #= True, esta en la lista
print(not True in tipos) #= False, esta en la lista pero lo negamos
print('hola' in tipos) #= True, esta en la lista

p = [2,3,5,7,11,13,17,19,23,29,31,37,41]
p[3:10:2]
print('--->',4 != 10)