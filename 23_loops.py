# loops

#-> Lista con listas dentro
matrix = [[1,2,3],[4,5,6],[7,8,9],]

#-> mostramos index 0 
print(matrix[0])

#-> ingresamos como coordenadas
print(matrix[0][1])
#dentro del index 1, accede al elemento 1

#-> for anidados
for i in matrix:
    print('items->',i)
    for e in i:
        print('elementos->',e)