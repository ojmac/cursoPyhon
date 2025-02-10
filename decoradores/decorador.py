"""
UN decorador es una funcion que agrega funcionalidad extra
a otra funcion sin modificar su estructura 

Objetos de primera clase : son objetos que pueden ser pasados a
una fucion, pueden ser retornados por una función, y pueden ser 
asignados a una variable

Los decoradores pertenecen al patrón de diseño "Decorador"
Estos permiten modificar la fucionalidad de un objeto de forma dinámica
Estas fucniones pueden ser usadas juntos ocn otras fuciones para extender sus capacidades 
din moficicarlas
Por definición, un decorador es una funcion que recibe una fucncion le agrega mas fucnionalidad y
retiorna la función modificada.

"""
def funcion_decorador(funcion):
    def funcion_wrapper():
        print("Dentro de la funcion_wrapper")
        funcion()
    return funcion_wrapper

def funcion_prueba():
    print("Esto es una prueba")

funcion_prueba = funcion_decorador(funcion_prueba) 

funcion_prueba()

@funcion_decorador
def funcion_prueba2():
    print("Esto es una prueba2")

funcion_prueba2()