sensor = True

def desactivar_sensor():
    global sensor # Con global se puede modificar la variable global
    print(sensor)
    if sensor == True:
        sensor = False
   

desactivar_sensor()
print(sensor)   

def activar_sensor():
    sensor = True
    print(sensor) 
    return  sensor

print(desactivar_sensor()) 
