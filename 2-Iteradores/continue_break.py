lista = [1, 2, 3, 4, 5] ;

for i in lista:
    print(i)    
    if i == 3:
        break
else:
    print("El bucle ha terminado")        

for i in lista:
    if i == 3:
        continue
    print(i)         
else:
    print("El bucle ha terminado")   
    
     