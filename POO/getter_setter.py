class Humano:

    def __init__(self, nombre, edad):
        self.__edad = edad
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        if edad < 0:
            self.__edad = 0
        else:
            self.__edad = edad  

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

javier = Humano('Javier', 25)

print(javier.edad)  
javier.edad = 26
print(javier.edad)

javier.edad = -1    
print(javier.edad)  # 0 

print(javier.nombre)
javier.nombre = 'Javier Rodriguez'
print(javier.nombre)
