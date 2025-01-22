def calcular_cuadrado(numero):
    return numero ** 2  

lista = [1,2,3,4,5,6,7,8,9,10]  
lista_pares = []        

for numero in lista:
    cuadrado = calcular_cuadrado(numero)    
    if cuadrado % 2 == 0:
        lista_pares.append(cuadrado)
        print(f"El cuadrado de {numero} es {cuadrado} y es par")    
    else:
        print(f"El cuadrado de {numero} es {cuadrado} y es impar")  

print("-----------------------------------------------------------")

for numero in lista:
    if(cuadrado:= calcular_cuadrado(numero)) % 2 == 0:
        lista_pares.append(cuadrado)
        print(f"El cuadrado de {numero} es {cuadrado} y es par")    
    else:
        print(f"El cuadrado de {numero} es {cuadrado} y es impar")

# walrus operator
#   :=                  
#  Asigna un valor a una variable y devuelve ese valor. 
# Es útil para asignar valores a variables dentro de expresiones.   
#                                               
#  Ejemplo: 
# for numero in lista:
#    if(cuadrado:= calcular_cuadrado(numero)) % 2 == 0:
#      lista_pares.append(cuadrado) 
#     print(f"El cuadrado de {numero} es {cuadrado} y es par")
#   else:
#    print(f"El cuadrado de {numero} es {cuadrado} y es impar")

list_comprenhesion = [cuadrado for numero in lista if (cuadrado:= calcular_cuadrado(numero)) % 2 == 0]  
print(list_comprenhesion) # [4, 16, 36, 64, 100]

# walrus operator otro ejemplo

datos = input("Ingrese algo: ")   

while datos != "salir":    
    print(f"Dijiste {datos}")    
    datos = input("Ingrese algo: ")

while(datos:= input("Ingrese algo: ")) != "salir":    
    print(f"Dijiste {datos}")       

    