def calcular_perimetro(*lados):
    perimetro = 0   
    for lado in lados:  
        perimetro += lado   

    return perimetro    # Devuelve el perímetro del polígono    

print(calcular_perimetro(5, 10, 15, 20))    # Imprime 50    # Llamada a la función con 4 argumentos 5, 10, 15, 20   

def calcular_perimetro2(*lados):
    perimetro = sum(lados)

    return perimetro    # Devuelve el perímetro del polígono

print(calcular_perimetro2(5, 10, 15, 20))    # Imprime 50    # Llamada a la función con 4 argumentos 5, 10, 15, 20  


