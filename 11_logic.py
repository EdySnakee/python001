# AND operador logico
print('AND') 
# Las dos partes de la operacion 
#tienen que ser verdad para regresar TRUE
print('True and True =>', True and True)     #-> TRUE
print('True and False =>', True and False)   #-> FALSE
print('False and True =>', False and True)  #-> FALSE
print('False and False =>', False and False) #-> FALSE

print(10 > 5 and 5 < 10) #->las dos operaciones se cumplen TRUE
print(10 > 5 and 5 < 10) #->SI SOLO UNA SE CUMPLE FALSE

#.> EJEMPLO DE STOCK
 
stock = int(input('Ingresa el stock ->'))

print(stock >= 50 and stock <= 100) 
#-> Una validacion, si tenemos suficiente stock
# regresa TRUE, amdas condiciones se tienen que cumplir



#==> OR operador logico, a diferencia de 'and' aqui solo se tiene que cumplor una
print('OR') 
# SI UNA CONDICION SE CUMPLE REGRESARA TRUE
print('True or True =>', True or True)     #-> TRUE
print('True or False =>', True or False)   #-> TRUE
print('False or True =>', False or True)  #-> TRUE
print('False or False =>', False or False) #-> FALSE


#-> Ejemplo de uso
role = input('role?=>') #-> Asignamos el valor de rol
print(role == 'a' or role == 'rh') 
#> si el valor es 'a' or 'rh', regresaremos TRUE, 
# podria ser una validación para login
