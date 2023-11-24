# Boolean solo pueden contener True : False (primera letra Mayus)

#Verificando tipo de dato
gordo = True
print(type(gordo)) #res => <class 'bool'>
gordo = False
print(gordo) #res => 'False'>


#transformaciones
#invertir
print('not', not True) 
print('not',not False) 

#Cambiamos su ultimo estado por el contrario
gordo = not gordo
print(gordo) #res => True

