'''Estructura de datos inmutables que contiene una secuencia ordenada de elementos
Es inmutable y por lo tanto no puede ser modificada, lo que permite proteger mejor la data si no queremos que se modifique por error'''


num = (1,2,3,4,5,6,)
string = ('pal-1','pal-2','pal-3','pal-4',)
print(num,string)
print(type(num),type(string)) #MOSTRAMOS EL TIPO DE DATO 'tupla'

 #PODEMOS ACCEDER A LOS DATOS DESDE EL INDEX
print('0 =>', num[0])
print('-1 =>', string[-1])


#A defierencia de las listas en las tuplas no tenemos accesos a los metodos de CRUD (inmutables)

# metodos de busqueda
palabras = ('cosa','tasa','hacha','amaca',)

#buscamos conincidencias
print(palabras.index('hacha'))

#cuantas coincidencias hay
print('conteo->' ,palabras.count('amaca'))

#TRASFORMACIONES
#-> la func list trasforma de tupla a list [ array]
lista = list(palabras)
print('tranformada en lista->', lista)

#ahora como lista podemos editar
lista[0]='editada'
print(lista)

#podemos trasformar una lsita en una tupla
new_tubla = tuple(lista)
print('Resultado->', new_tubla,'tipo->', type(new_tubla))