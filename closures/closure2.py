def operar (numero):
    def transforma_valor(x):
        return x * numero
    return transforma_valor   

duplicar = operar(2)
triplicar = operar(3)
print(duplicar(5))
print(triplicar(5))

def operar2 (numero):
    local = 7
    def transforma_valor(x):
        nonlocal local
        local +=1 ;
        return local + 1
       # return x * numero
    return transforma_valor  