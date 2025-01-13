cuadrados = [1, 4, 9, 16, 25]   
print(cuadrados)    
print(cuadrados[0]) 
print(cuadrados[-1])    
print(cuadrados[-3:])   
print(cuadrados[2:]) 

cuadrados = cuadrados + [36, 49, 64, 81, 100]   
print(cuadrados)    

cuadrados[3] = 1000
print(cuadrados)

cuadrados.append(121)   
print(cuadrados)    

cubos = [1, 8, 27, 65, 125]
cubos[3] = 64   
cubos.append(6**3)  
cubos.append(343)  
print(cubos)    

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']    
print(len(letras))  
rgb = ['rojo', 'verde', 'azul'] 
rgba = rgb # argb es una referencia a rgb   
rgba.append('alpha') 
print(rgb)  
print(rgba)
 # Para copiar una lista se puede hacer con la función list()
copia_rgb = list(rgb)   
rgba_corregida = rgba[:] # Otra forma de copiar una lista

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']    
letras[2:5] = ['C', 'D', 'E']   
print(letras)   
letras[2:5] = []    
print(letras)   
letras[:] = []      
print(letras)   
a = ['a', 'b', 'c'] 
n = [1, 2, 3]   
x = [a, n]  
print(x)    
print(x[0]) 

