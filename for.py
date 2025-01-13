palabras = ['gato', 'ventana', 'elefante']  
for p in palabras:  
    print(p, len(p))    
print('Fin del programa')   # Imprime: Fin del programa 

for  i in range(5):
    print(i) # Imprime: 0 1 2 3 4   

for i in range(5, 10):
    print(i) # Imprime: 5 6 7 8 9   

for i in range(0, 10, 3):       
    print(i) # Imprime: 0 3 6 9     

for i in range(-10, -100, -30):      
    print(i) # Imprime: -10 -40 -70 

a = ['Mary', 'tenia', 'un', 'corderito']    
for i in range(len(a)):    
    print(i, a[i]) # Imprime: 0 Mary 1 tenia 2 un 3 corderito   

dicionario = {'a': 1, 'b': 2, 'c': 3}  
for key in dicionario:    
    print(key, dicionario[key]) # Imprime: a 1 b 2 c 3 

for key, value in dicionario.items():
    print(key, value) # Imprime: a 1 b 2 c 3

for key, value in dicionario.copy().items():    
    if value == 2:        
        del dicionario[key] # Elimina el valor 2 del diccionario
dicionarioVacio = {}    

for key, value in dicionario.items():  
    if value == 1:    
        dicionarioVacio[key] = value    

print(dicionarioVacio) # Imprime: {'a': 1}

for i, v in enumerate(['tic', 'tac', 'toe']):    
    print(i, v) # Imprime: 0 tic 1 tac 2 toe    

preguntas = ['nombre', 'objetivo', 'color favorito']    
respuestas = ['lancelot', 'el santo grial', 'azul'] 
for p, r in zip(preguntas, respuestas):    
    print('Cual es tu {0}? {1}.'.format(p, r)) # Imprime: Cual es tu nombre? lancelot. Cual es tu objetivo? el santo grial. Cual es tu color favorito? azul.    

for i in reversed(range(1, 10, 2)):    
    print(i) # Imprime: 9 7 5 3 1   

