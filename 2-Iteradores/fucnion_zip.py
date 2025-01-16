nombre = ['Juan', 'Pedro', 'Luis']
apellidos = ['Perez', 'Gomez', 'Gonzalez']  # Se pueden agregar más listas
edades = [20, 30, 40]   

for n, a, e in zip(nombre, apellidos, edades):  
    print(f'{n} {a} tiene {e} años')    # Se pueden agregar más variables

nombre_completo = zip(nombre, apellidos)    # Se puede guardar en una variable
print(list(nombre_completo))    # Se puede convertir a una lista


nombre_completo_edad= zip(nombre, apellidos, edades)    # Se pueden agregar más listas  
print(list(nombre_completo_edad))    # Se puede convertir a una lista

nombre_completo_lista = [list(tupla) for tupla in zip(nombre, apellidos)]
print(nombre_completo_lista)

nombre_completo_edad_lista = [list(tupla) for tupla in zip(nombre, apellidos, edades)]
print(nombre_completo_edad_lista)

nombre_completo_diccionario = {tupla[0]: tupla[1] for tupla in zip(nombre, apellidos)}  # Se puede convertir a un diccionario   
print(nombre_completo_diccionario)  # Se puede convertir a un diccionario   

nombre = ['Juan', 'Pedro', 'Luis']
apellidos = ['Perez', 'Gomez', 'Gonzalez']  # Se pueden agregar más listas

nombre_completo = zip(nombre, apellidos)    # Se puede guardar en una variable  

nombre_unzip, apellido_unzip = zip(*nombre_completo)    # Se puede descomprimir 
print(nombre_unzip)
print(apellido_unzip)   # Se puede descomprimir 

nombre = ['Juan', 'Pedro', 'Luis']  
apellidos = ['Perez', 'Gomez', 'Gonzalez']  # Se pueden agregar más listas

nombre_completo = zip(nombre, apellidos) 

edad = [20, 30, 40] 
altura = [1.70, 1.80, 1.90]  # Se pueden agregar más listas

edad_altura = zip(edad, altura) 

total_datos = zip(nombre_completo, edad_altura)  # Se pueden agregar más variables
print(list(total_datos))  # Se pueden agregar más variables

nombre = ['Juan', 'Pedro', 'Luis']
apellidos = ['Perez', 'Gomez', 'Gonzalez']  # Se pueden agregar más listas
edades = [20, 30, 40]   

nombre_apaellidos_edades = zip(nombre, apellidos, edades)  # Se pueden agregar más listas   
print(list(nombre_apaellidos_edades))  # Se pueden agregar más listas

nombre_unzip, apellido_unzip, edad_unzip = zip(*list(zip(nombre, apellidos, edades)))  # Se pueden agregar más variables   
print(nombre_unzip)  # Se pueden agregar más variables
print(apellido_unzip)  # Se pueden agregar más variables
print(edad_unzip)  # Se pueden agregar más variables 