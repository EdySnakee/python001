# CRUD Create, Read, Update, Delete

#-> Creamos
num = [1,2,3,4,5,6]

#->leemos
print(num[5])

#-> Editamos
num[-1] = 10
print(num)

#-> Agregamos / podemos agregar cualquier tipo de dato
num.append(333) #-> Agrega al final de la lista
print(num)

num.insert(0,15) #-> Agrega en i[0] de la lista
print(num)

num.insert(3,'change') #-> Agrega en i[3] de la lista
print(num)


#-> Uniendo listas
tareas = ['tar1','tar2','tar3']
new_lista = num + tareas
print(new_lista)

#> Preguntar en donde esta un elemento de la lista
print(new_lista.index('tar2'))
index = new_lista.index('tar2') #-> Asignamos

#> Actualizamos
new_lista[index] = 'tar edit'
print(new_lista)


#-> remove
new_lista.remove('change') #-> remove el parametro enviado
print(new_lista)

new_lista.pop() #-> removemos el ultimo elemento de la lista
print(new_lista)

new_lista.pop(0) #-> remove el elemento del index enviado
print(new_lista)


#-> reverse
new_lista.reverse() #-> cambia el sentido de la lista en reverse
print(new_lista)


#-> Sort
num2 = [1,3,4,6,2,5]
num2.sort() #-> cambia el orden de la lista <  >
print(num2)

strings = ['re','ab','ed','ee']
strings.sort() #-> cambia el orden de la lista alfabeticamente
print(strings)
