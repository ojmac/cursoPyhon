fecha = "01-01-2025"

def fucion_scope_local():

    global fecha
    nombre = "javier"

    return nombre

#funcion anidada

def funcion_primera():
    nombre = "javier"
    def anidada():
        print (nombre)
    anidada()

print(funcion_primera())

# un closure necesita una fucnion anidada para fucionar
# la funcion anidada debe usar o referencia una variable del scope superior
# la funcion que contiene la funcion anidada debe retornar la funcion anidada

def saludar():
    menasje = "Buen dia"
    def imprimir_saludo():
        print(menasje)
    return imprimir_saludo

saludo = saludar()
print(saludo())

