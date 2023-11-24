# los numero al igual que los string, se pueden re asignar

# numero entero
x = 5
print(x)

# numero entero re asignado
x = 6
print(x)

# numeros flotantes se distinguen por el decimal
y = 5.5
print(y)

# numeros complejos, en este ejemplo le asignamos a la variable, #el resultado de la ope
z = 3 + 5
print(z)

#- operaciones matematicas
# suma
print('+ =>',3 + 5)
# resta
print('- =>',3 - 5)
# multiplicacion
print('+ =>',3 * 5)
# division
print('/ =>',3 / 5)
# division entera
print('// =>',3 // 5)
# potencia
print('** =>',3 ** 5)
# modulo
print('% =>',3 % 5)


#- operaciones
money = 33 + 3
print('init->',money)

#Ahora le restamos 3
money = money - 3
print('2->',money)

#Ahora sumamos 7
money += 7
print('3->',money)

# Numeros grandes
numero = 3333333333333333333333333333333333.3
print(numero)

# Numeros pequeños
numero2 = 0.0000000000000000000000001
print(numero2)


#RECUERDA NOMBRAR LAS VARIABLES CON NOMBRES QUE REFLEJEN SU CONTENIDO

ene = 100
mar = 200
abr = 300
presupuesto = ene + mar + abr
text = f"enero: {ene}, marzo: {mar}, abril: {abr}, = {presupuesto/3}"
print(text) #sacamos el promedio del presupuesto