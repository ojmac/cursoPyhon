import csv

columnas = ['Nombre', 'Apellidos', 'Edad']  
dato = ['Juan', 'Perez', 25]   

datos=[['Juan', 'Perez', 25], ['Maria', 'Gomez', 30], ['Pedro', 'Garcia', 35]]

datos_dic = [
    {"nombre": "Juan", "apellido": "Perez", "edad": 25},
    {"nombre": "Maria", "apellido": "Gomez", "edad": 30},
    {"nombre": "Pedro", "apellido": "Garcia", "edad": 35}
]

with open("datos_dic.csv", "w", encoding="UTF_8") as Archivo_dic:
    writer = csv.DictWriter(Archivo_dic, fieldnames=datos_dic[0].keys())
    writer.writeheader()
    writer.writerows(datos_dic)

archivo = open('empleados2.csv', 'w')   
writer = csv.writer(archivo, delimiter=',')
archivo.close()

#with open('empleados2.csv', 'w',encoding="UTf-8") as archivo:    
with open('empleados2.csv', "w", newline="") as archivo:
    writer = csv.writer(archivo, delimiter=',') 
    writer.writerow(columnas)
    writer.writerows(datos)