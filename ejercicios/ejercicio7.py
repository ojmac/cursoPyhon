#calculadora usando closures

def crear_operacion(operador ="suma"):
    def operacion(a,b):
        if operador == "suma":
            return a + b
        elif operador == "resta":
            return a - b
        elif operador == "multiplicacion":
            return a * b
        elif operador == "division":
            if(b!=0):
                return a / b
            else:
                return "No se puede dividir por cero"
    return operacion

sumar = crear_operacion("suma")

print (sumar(2,7))
