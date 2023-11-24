# if trabajando con condiciones

#- Si la condicion se cumple, ejecuta el codigo
if True:
    print('ejecuta')

if  False:
    print('nunca')
    

#- if se ejecuta si se cumple la instrucción
pet = input('Mascota fav?')
#- el valor ingresado, lo validamos con if si la condicion se cumple
# se ejecuta el codigo correspondient
if pet == 'pez':
    print('woooa')

if pet == 'gato':
    print('gato')


#- else -> SI EL IF NO SE CUMPLE EJECUTA EL ELSE*
'''
stock = int(input('stock?->'))
if stock >= 50 and stock <= 100:
    print('Correcto!')
else:
    print('Error')
'''

#- elif -> 
# SI EL PRIMER IF NO SE CUMPLE CONTINUA CON elif,
#- lanzamos otra pregunta
'''
num = int(input('adivina el numero->'))

if num == 3:
    print('Correcto')
elif num == 4:
    print('Error')
elif num == 5:
    print('Error')
else:
    print('numeros disponibles = 3.4.5')
''' 
 
#- Es par?  (ejemplo)

num = int(input('numero->'))
if num % 2 == 0:
    print('Es Par')
else:
    print('Es none')