##CICLOS FOR itema bajo un conjunto de datos (definido)

# range, crea iteraciones desde un rando dado
'''
for item in range(13): #en este caso hasta el 13 empezando en 0
    print(item)
    
for item in range(1,14): #asi lograriamos los numeros del 1 al 13
    print(item)
'''

# CICLOS EN LISTAS 
list = [33,22,44,66,77,11]
#de esta manera iteramos y hacermos en recorrido en la list->
for i in list:
    print(i)

#EN TUPLAS
tupla = ('lau','fer','mau','oto')
for i in tupla:
    print(i)
    

# DICCIONARIO
product = {
    'name': 'mazapam',
    'price': 10,
    'stock': 89
}

# AL USAR UN FOR EN DICC RETORNARA LAS keys QUE PODEMOS 
# USAR PARA ACCEDER A LOS DATOS
for i in product:
    print(i,'->', product[i])

#podemos obtenber el mismo resultado de forma directa
for key, value in product.items():
    print(key,'-->', value)


#Listas
people = [
    {
        'name': 'lau',
        'edad': 33
    },
    {
        'name': 'PAo',
        'edad': 35
    },
    {
        'name': 'Fred',
        'edad': 34
    },
    {
        'name': 'mat',
        'edad': 33
    }
]

for i in people:
    # print(i) #iteramos en toda la lista
    print('name->',i['name']) #accedemos al valor