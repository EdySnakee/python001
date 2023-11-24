#> VAMOS A MANIPULAR STRING'S 

##> f1 Buscar conincidencias dentro de la variable
texto = 'Ella sabe programar en c'
print('x' in texto) #> busca la letra dentro de la variable
print('sabe' in texto) #> busca la palabra dentro de la variable

##> f2 usamos if para cuestionar si 'js' existe en texto
if 'js' in texto:
    print('Ella sabe')
else:
    print('Que pena')

##> f3 len para saber cuantos caracteres tiene la variable 
tamaño = len('cache') 
print(tamaño)
#- Recuerda que si hay espacios en el texto, tambien contaran como caracteres.
tam1 = len(texto)
tam2 = len('ca') #-> 2
tam3 = len(' ca ') #-> 4 suma los espacios
print(tam2, tam3, tam1)


##_> f4
text = 'Texto de prueba'

#>Para convertirlo en mayusculas
print(text.upper())

#>Para convertirlo en minusculas
print(text.lower())

#>Para contar
print(text.count('e')) #- en este caso cuntas 'e' hay!

#>convertir mayusculas en minus y vice versa
print(text.swapcase())

#>Si el texto inicia con esta palabra regresa TRUE
print(text.startswith('Texto'))

#>Si el texto finaliza con esta palabra regresa TRUE
print(text.endswith('de'))

#>Para remplasar el texto con un valor asignable
print(text.replace('de', 'para'))

#- Texto 2
text2 = 'este es un baile'
print(text2)

#> Capitalize convierte la primera letra del texto en mayus
print(text2.capitalize())

#> title convierte la primera letra de cada palabra en mayus
print(text2.title())

#> Esto nos dice si es un digito
print(text2.isdigit()) #- False porque es string
print("333".isdigit()) #- TRUE identifica el digito 