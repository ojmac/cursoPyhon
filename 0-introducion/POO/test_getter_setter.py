class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

# Ejemplo de uso
persona = Persona("Juan")
print(persona.nombre)  # Salida: Juan
persona.nombre = "Pedro"
print(persona.nombre)  # Salida: Pedro