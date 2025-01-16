def funcion_kwargs(**kwargs):
    print(kwargs)    # Imprime {'nombre': 'Juan', 'edad': 25}    # Imprime el diccionario kwargs    
    for key, value in kwargs.items():    # Recorre el diccionario kwargs
        print(f'{key} = {value}')    # Imprime nombre = Juan y edad = 25   
        print (kwargs['nombre'])    # Imprime Juan    # Imprime el valor de la clave nombre del diccionario kwargs      

funcion_kwargs(nombre='Juan', edad=25)    # Llamada a la función con dos argumentos nombre='Juan' y edad=25     
  