#Diccionarios 

dict = {}
print('tipo->', type(dict))

# deficion
new_dict = {
    'cosa': 'string',
    'nombre': 'Fj77',
    'edad': 76,
    'vuela': False
}
print(new_dict)

#Conteo de elementos
print('numero de elementos->',len(new_dict))

#Accediendo a la data
print('accediendo al elemento->', new_dict['cosa'])
print('accediendo al elemento->', new_dict['edad'])

# usando get, obtenemos un 'none' en caso de error y lo podremos manejar
print('accediendo al elemento->', new_dict.get('nombre'))


#obteniendo un true o false 
print('cosa' in new_dict)
print('algo' in new_dict)

print(8000>3330)