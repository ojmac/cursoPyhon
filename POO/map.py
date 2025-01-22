def cuadrado(n):
    return n ** 2   

lista = [1, 2, 3, 4, 5, 6, 7, 8]

resultado = map(cuadrado, lista)    

print(list(resultado))  

