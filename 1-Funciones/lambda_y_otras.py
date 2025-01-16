#funcion lambda argumentos : expresion

funcion = lambda num: num * num
print(funcion(2))   # 4 

funcion = lambda x, y: x + y        
print(funcion(2, 3)) # 5    

funcion = lambda *args: args    
print(funcion(1, 2, 3)) # (1, 2, 3)

funcion = lambda **kwargs: kwargs
print(funcion(a=1, b=2)) # {'a': 1, 'b': 2}

#funcion filter 

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
pares = list(filter(lambda x: x % 2 == 0, lista))   
print(pares) # [2, 4, 6, 8, 10]

#funcion map

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
cuadrados = list(map(lambda x: x * x, lista))   
print(cuadrados) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]   

#funcion reduce

from functools import reduce
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     
suma = reduce(lambda x, y: x + y, lista)    
print(suma) # 55    

#funcion sorted

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = sorted(lista, key=lambda x: -x)
print(lista) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#funcion max    

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maximo = max(lista, key=lambda x: x)
print(maximo) # 10

#funcion min

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
minimo = min(lista, key=lambda x: x)
print(minimo) # 1

#funcion any

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
resultado = any(map(lambda x: x % 2 == 0, lista))
print(resultado) # True

#funcion all

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = all(map(lambda x: x % 2 == 0, lista))
print(resultado) # False

#funcion zip

lista1 = [1, 2, 3, 4, 5]
lista2 = ['a', 'b', 'c', 'd', 'e']
resultado = list(zip(lista1, lista2))
print(resultado) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

#funcion enumerate

lista = ['a', 'b', 'c', 'd', 'e']
resultado = list(enumerate(lista))
print(resultado) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

#funcion reversed

lista = [1, 2, 3, 4, 5]
resultado = list(reversed(lista))
print(resultado) # [5, 4, 3, 2, 1]
