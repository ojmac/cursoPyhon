

import csv
import os
# Crear un archivo CSV

file = open('empleados.csv', 'w')
writer = csv.writer(file, delimiter=';')
file.close()

pwd = os.getcwd()   
print(pwd)

ruta_absoluta = os.path.abspath('empleados.csv')   # Ruta absoluta
ruta_absoluta = os.path.join(pwd, 'empleados.csv')   # Añadir a ruta absoluta

# Escribir encabezados

writer.writerow(['Nombre', 'Puesto', 'Salario'])    

# Escribir datos

writer.writerow(['Juan', 'Gerente', 1000])

# Cerrar archivo

file.close()


# Leer un archivo CSV

file = open('empleados.csv', 'r')

reader = csv.reader(file, delimiter=';')    

for row in reader:
    print(row)  

file.close()    

# Agregar datos a un archivo CSV    

file = open('empleados.csv', 'a')

writer = csv.writer(file, delimiter=';')    

writer.writerow(['Pedro', 'Contador', 800]) 


