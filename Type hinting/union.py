from typing import Union



def cuadrado(lado: Union[int, float])-> Union[int,float]:
    return 3*lado

print(cuadrado(3))
print(cuadrado(3.1))
print(cuadrado("pepe"))

