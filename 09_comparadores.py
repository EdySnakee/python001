#> MAyor que
print(7>3) #las comparaciones nos regresaran un True o False
print(5>7) #False


# < MENOR que
print(5<6) #TRue
print(6<5) #False


# >= MAYOR O IGUAL que
print(2>=2)
print(2>=3)

# >= MENOR O IGUAL que
print(2<=1)
print(2<=3)


# == IGUALDAD
print(2==1)
print(3==3)


# != COMPARACIÓN 
print( 6 != 10 ) # -> 6 es diferente a 10 #TRUE
print( 10 != 10 ) # -> 10 es diferente a 10 #FALSE
 
# ala misma palabra el cambio de comillas no le afecto, pero si el cambio de Mayus
print("Apple" == 'Apple') #TRUE
print("Apple" == 'apple') #FALSE <= 

print("1" == 1) #FALSE No son el mismo tipo de dato

#Caso de uso con variable
edad = int(input("Ingresa tu edad =>")) # valor introducido por el user
print('e=>',edad >= 18) 
# si es mayor >= de 18 regresa TRUE, que bien 
#se puede usar como logica de negocio para dar o denegar accesos-