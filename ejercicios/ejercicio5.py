"""Crear una clase de nmbre perosna que tenga los siguientes atributos: nombre y edad
y un atributo id autoincrmental. """

class Persona:
    next_id = 0
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        Persona.next_id += 1
        self.id = Persona.next_id

