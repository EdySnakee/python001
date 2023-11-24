#-> Not, un operador de negacion

print(not True) #- print FALSE -> not niega su estado original
print(not False) #-print TRUE -> not niega su estado original

# ->
print(' NOT AND') 
print('True and True =>', not (True and True))     #-> FALSE
print('True and False =>', not (True and False))   #-> TRUE
print('False and True =>', not (False and True))  #-> TRUE
print('False and False =>', not (False and False)) #-> TRUE
#-> Con el operador cambiamos todos los resultados, ahora que
# estan negados, podemos ver que ' t and t' nos puede dar false

# ->
stock = int(input('Ingresa el stock ->')) #-> 13
print( not(stock >= 50 and stock <= 100)) #-> True
#- En este caso si el valor ingresado, no cumple con 
# ninguna condicion tendremos un TRUE