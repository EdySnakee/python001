# Aqui declaramos las variables, podemos
# usar comillas dobles o sencillas
nombre = "Juan"
apellido = 'Perez'
# Aqui hacemos una concadenacion de strings
nombre_completo = nombre + " " + apellido
print(nombre_completo)

#- Mezclando las comillas =>
frase = "I'm power"
print(frase)

frase2 = 'you "not"'
print(frase2)

#- formato
#las tres versiones nos regresan el mismo resultado

#v1
template = "My name is {} {}"
print('1 =>', template.format(nombre, apellido))
#v2
template = "My name is {} {}".format(nombre, apellido)
print('2 =>', template)
#v3
template = f"My name is {nombre} {apellido}"
print('3 =>', template)

#Otra forma de concatenar strings
template2 = "Mi nombre es " + nombre + " y mi apellido es " + apellido
print('=>', template2)

#=> 
marca = 'HP'
modelo = 'Pavillion'
price = 333
#
pc = f"La marca de mi pc es '{marca}' y el modelo es {modelo} y el precio es ${price}"
print(pc)
#
pc= f"Una marca {marca}, y mira el precio $ {price}, te los vas a perder {modelo}"
print(pc)
