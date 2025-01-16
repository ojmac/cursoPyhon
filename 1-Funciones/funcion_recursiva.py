def calcular_factorial(n):
    if n == 0 or n == 1:    # Caso base                 
        return 1            
    else:            # Caso recursivo   
        return n * calcular_factorial(n - 1)                    

n = 5
print(f"El factorial de {n} es {calcular_factorial(n)}")    

import sys  

#sys.setrecursionlimit(10000)  # Cambiar el límite de recursión  
#n = 1000
#print(f"El factorial de {n} es {calcular_factorial(n)}")    

try:
    n = 90
    print(f"El factorial de {n} es {calcular_factorial(n)}")    
except RecursionError as e:
    print(f"Error: {e}")
    print("Se ha excedido el límite de recursión")
    print("Cambie el límite con sys.setrecursionlimit(10000)")
except Exception as e:
    print(f"Error: {e}")
    print("Ha ocurrido un error")  
else:
    print("No ha ocurrido ningún error")         
finally:
    print("Fin del bloque try-except")  
    sys.exit()
    
print("Fin del programa")   


