
# MIENTRAS LA CONDICION SEA True,
'''
while True:
    print('se ejecuta')
'''

## ejemplo funcional
'''
contador = 0
while contador < 6:
    contador += 1
    print('con->',contador)
    
'''

## ejemplo 2 podemos detener el while, 
# de una manera forzada si es necesario
'''
contador = 0 

while contador < 10:
    contador += 1
    if contador == 7:
        break
    print('frenado',contador)
'''


## ejemplo 3 usando continue, python continua con la siguiente iteracion
# si hay mas logica debajo, no sera leida despues del 'continue'
 
contador = 0

while contador < 10:
    contador += 1
    if contador < 6:
        continue
    print('saltado',contador) 
#Solo inprimimos del 6 en adelante, por el continue