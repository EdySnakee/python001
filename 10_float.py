# Los desimales pueden causar errores facilmente, ya que la presición
# de los valores tendra peso en la comparación
#->
x = 3.3
print(x)

y = 1.1 + 2.2
print(y)

print(x==y) #FALSE -> Ya que los valores de Y incluyen decimales

#- COMPARARTO VALUES

#.>f1
y_srt = format(y,".2g") 
#modificamos y para que solo tenga dos dig y convertimos a str =>
print(y_srt)  
#Ahora convertimo x, y comparamos
print(y_srt == str(x)) #TRUE -> ahora la comparacion es exitosa


#.>f2
print(y,x)
tolerancia = 0.0001
print(abs(x -y) < tolerancia) #TRUE ->
#Ya que tenemos una tolerancia al momento de restar y de x y comparar con tolerancia, obtenemos un true. 

i = (abs(x-y))
print(i < tolerancia ) #TRUE ?????
