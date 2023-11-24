# se puede cambiar el tipo de dato de forma dinamica
#string
let = "string"
print(type(let))
#number
let = 33
print(type(let))
#boolean
let = False
print(type(let))

# como parte de la flexibilidad de py podemos asignar cualquier valor a variables
# Recuerda que dependiento el tipo py hara cosas diferentes

print("string1 " + "string2")  # concatenara
print(20 + 20)  # sumara los valores
# print("string1" + 20) # ERROR

# Para cambiar el tipo de dato de una variable usamos el operador de casting
print(str(let)) # convierte a string
print(int(let)) # convierte a numero entero
print(float(let)) # convierte a numero flotante
print(bool(let)) # convierte a 

#-Usando f (format) podemos darle formato a nuestras variables
edad = 12 
print('Mi edad es '+ str(edad)) #-> evitamos esto usando ->
print(f'Mi edad es {edad}', type(edad))


#- 'Input siempre nos regresara un string'

num = input('¿Cúal es tu numero fav => ')
print(type(num)) #revizamos el tipo
print(f'nuestros nuemeros suman {(int(num)) + 13}')

#forma 2
num2 = input('¿Cúal es tu numero fav => ')
num2 = int(num2)
print(type(num2)) #revizamos el tipo
num2 += 13
print(f'nuestros nuemeros suman {num2}')

#forma 3
edad = int(input("Ingresa tu edad =>"))
print(edad, 'tipo = ', type(edad))


print((8 / 2) + 4 * 8)