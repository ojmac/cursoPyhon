# lista = [expression for item in iterable if condition == True]

# List comprehension

cuadrados = [n ** 2 for n in range(1, 9)]   
print(cuadrados) # [1, 4, 9, 16, 25, 36, 49, 64]    

def cuadrados(n):
    return n ** 2       

lista = [cuadrados(n) for n in range(1, 9)] 
print(lista) # [1, 4, 9, 16, 25, 36, 49, 64]

# List comprehension with condition
# [expression for item in iterable if condition == True]


pares = [n for n in range(1, 9) if n % 2 == 0]
print(pares) # [2, 4, 6, 8]

 
cuadrados2 = [lambda n: n ** 2 for n in range(1, 9)]    

print(cuadrados2) # [<function <listcomp>.<lambda> at 0x7f8b1c1b7d30>, <function <listcomp>.<lambda> at 0x7f8b1c1b7d08>, <function <listcomp>.<lambda> at 0x7f8b1c1b7e18>, <function <listcomp>.<lambda> at 0x7f8b1c1b7ea0>, <function <listcomp>.<lambda> at 0x7f8b1c1b7f28>, <function <listcomp>.<lambda> at 0x7f8b1c1b7f98>, <function <listcomp>.<lambda> at 0x7f8b1c1b8048>, <function <listcomp>.<lambda> at 0x7f8b1c1b80d0>]  

cuadrados2 = [(lambda n: n ** 2)(n) for n in range(1, 9)]   
print(cuadrados2) # [1, 4, 9, 16, 25, 36, 49, 64]   

# [expression if condition == True else other_expression for item in iterable]

pares = [n if n % 2 == 0 else "Impar"for n in range(1, 9)] 
print(pares) # ['Impar', 2, 'Impar', 4, 'Impar', 6, 'Impar', 8] 

#list comprehension with nested loops   

lista = [(x, y) for x in range(1, 3) for y in range(1, 3)]  
print(lista) # [(1, 1), (1, 2), (2, 1), (2, 2)] 

#list comprehension with nested loops and condition 

lista = [(x, y) for x in range(1, 3) for y in range(1, 3) if x != y]
print(lista) # [(1, 2), (2, 1)]

#list comprehension_set

lista = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]   

set_pares = {n for n in lista if n % 2 == 0}    
print(set_pares) # {2, 4, 6}

set_impares = {n for n in lista if n % 2 != 0}  
print(set_impares) # {1, 3, 5}  

#list comprehension_dict

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

diccionario = {n: n ** 2 for n in lista}    
print(diccionario) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

diccionario = {n: "par" if n % 2 == 0 else "impar" for n in lista}  
print(diccionario) # {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar', 6: 'par', 7: 'impar', 8: 'par', 9: 'impar', 10: 'par'}    


