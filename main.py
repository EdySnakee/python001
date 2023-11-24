# JUEGO DE PIEDRA PAPEL Y TIJERA


import random

#CREAMOS UNA TUPLA PARA MEJOR MANEJO DE OPCIONES
opciones = ('piedra', 'papel', 'tijera')
r = 1
pc_wins = 0
user_wins = 0

while True:
    
    print('*' * 7)
    print('ROUND', r)
    print('*' * 7)
    print('*'*3,'Tú = ', user_wins,'*'*3)
    print('*'*3,'Pc = ', pc_wins,'*'*3)
    
    

    usuario =  input('piedra, papel o tijera ->').lower()
    r += 1

    #verificamos la seleccion de user
    if not usuario in opciones:
        print('¿Quieres jugar o no?')
        continue


    pc = random.choice(opciones)

    print('usuario->', usuario)
    print('pc->', pc)


    if usuario == pc:
        print('Empate!')

    #> caso 1  
    elif usuario == 'piedra':
        if pc == 'tijera':
            print('Ganaste')
            user_wins += 1
        else:
            print('Perdiste')
            pc_wins += 1
    #> caso 2        
    elif usuario == 'papel':
        if pc == 'tijera':
            print('Perdiste')
            pc_wins += 1
        else:
            print('Ganaste')
            user_wins += 1

    #> caso 3
    elif usuario == 'tijera':
        if pc == 'piedra':
            print('Perdiste')
            pc_wins += 1
        else:
            print('Ganaste')
            user_wins += 1
    if pc_wins == 2:
        print('*'*3, 'PC GANA','*'*3)
        break
    if user_wins == 2:
        print('*'*3, 'USER GANA','*'*3)
        break
    
    
    