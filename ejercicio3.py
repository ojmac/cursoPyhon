
"""Los números de las claves de dos caja fuertes están mezcladas en un
número entero llamado clave maestra. Determnie ambas claves, la primera clave se construye
con los digitos impares de la clave maestra y la segunda con los pares.
ejemplo :clave Meastra 12345, clave1 =135,clave2=24;"""

num = input("Escribe la contraseña maestra: ")

def claveMaestraKeys (num):
   
    clave1 = []
    clave2 = []
    
    for n in num:
        if cont%2==0:
            clave1.append(n)            
            
        else:
            clave2.append(n)
            
    print ("Clave Maestra = " +  num + ", clave1 = " + clave1 + ", clave2 =  " + clave2)

claveMaestraKeys(num)