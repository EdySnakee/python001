#-> INDICADOR EN LOS TEXTOS, PARA INGRESAR A NIVEL DE POSISIONES
#- los espacios entre palabras no son numerados

text = 'Ella esta barbara'

#- INGRESANDO POR INDEX
print(text[0]) #> EN PY LA PRIMERA POSITION ES CERO
print(text[6]) #_> 's'
''' print(text[100])''' #> DARA ERROR SI EL NUMERO EXCEDE EL INDEX


#> BUSCANDO EL ULTIMO CARACTER
size = len(text)
print(text[size-1]) #>RESTAMOS 1, YA QUE SIZE INICIA EN 1

#-f2
print(text[-2]) 
print(text[-1]) 
#> py entiende -1 como la ultima posición del text 


#> slicing obtendra el subtext dentro de la posicion marcada
print(text[0:4]) # Ella
print(text[10:17]) # barbara
print(text[:7]) # si no enviamos valor por defecto inicia en 0 
print(text[7:]) # si no enviamos valor por defecto termina -1 
print(text[:]) # desde el inicio hasta el final 
print(text[10:17:1]) # el ultimo digito son los saltos
print(text[10:17:2]) # aqui notamos el cambio
print(text[::2]) # del inicio al final saltando dos elementos


