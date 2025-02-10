"""
Mediante un Clousure hacer un contador que devuelve un numero de cuenta siguiente cada vez
que se le llame a la funcion clousure.

La fución de creación del contador recibe dpos parametros. En valor de incio que por defecto
será cero y el iccremento que debe hacerse cada vez que se llama a la fucion clousure,
tendra un valor pordefecto de 1.

"""

def funcion_contador(inicial=0):
    contador = inicial
    def clousure_contador(incremento=1):
        nonlocal contador
        contador += incremento
        return contador
    return clousure_contador

contador = funcion_contador(10)
print(contador(2))