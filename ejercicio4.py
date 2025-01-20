"""Ejercicio: Sistema de Gestión de Vehículos
Contexto
    Eres un desarrollador encargado de crear un sistema para gestionar diferentes tipos de vehículos
    en una empresa de transporte. Los vehículos pueden ser autos, motocicletas y camiones.
    Cada tipo de vehículo tiene características comunes, pero también algunas propiedades únicas.

Instrucciones
    Crea una clase base llamada Vehiculo con los siguientes atributos y métodos:

    Atributos comunes:
        marca (cadena): Marca del vehículo.
        modelo (cadena): Modelo del vehículo.
        año (entero): Año de fabricación.
    Métodos:
        __init__: Para inicializar los atributos comunes.
        mostrar_info: Imprime la información del vehículo en un formato legible.
        calcular_antiguedad: Devuelve la antigüedad del vehículo en años.
        Crea tres clases derivadas de Vehiculo:

    Auto:
        Atributo adicional: cantidad_puertas (entero).
        Sobrescribe el método mostrar_info para incluir la cantidad de puertas.
    Motocicleta:
        Atributo adicional: tipo (cadena, por ejemplo: "Deportiva", "Chopper").
        Sobrescribe el método mostrar_info para incluir el tipo de motocicleta.
    Camion:
        Atributo adicional: capacidad_carga (flotante, en toneladas).
        Sobrescribe el método mostrar_info para incluir la capacidad de carga.

En la función principal:

Crea una lista de vehículos con al menos:
    1 objeto de tipo Auto.
    1 objeto de tipo Motocicleta.
    1 objeto de tipo Camion.

    Usa un bucle para recorrer la lista y llamar a los métodos mostrar_info y calcular_antiguedad para cada vehículo.

    Agrega un método en la clase base llamado es_moderno que devuelva True si el vehículo tiene menos de 5 años de antigüedad.
    Implementa un método estático en la clase base para calcular la diferencia en años entre dos vehículos."""
from datetime import datetime

class Vehiculo:


    def __init__(self, marca, modelo, anyo):
       
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo

   
    def mostrarInfo(self):
        print(f"Vehiculo marca: {self.marca}, modelo: {self.modelo} del año {self.anyo}.")

  

    def mostrarAntiguedad(self):
           anio_actual = datetime.now().year
           ant = anio_actual - self.anyo 
           print(f"La edad de este vehículo es de: {ant} ")
           return ant

# Crear una instancia de Vehiculo
mi_vehiculo = Vehiculo("Toyota", "Corolla", 2020)

# Mostrar información del vehículo
mi_vehiculo.mostrarInfo()
mi_vehiculo.mostrarAntiguedad()

class Auto(Vehiculo):
     

    def __init__(self, marca, modelo, anyo, numPuertas):

        super().__init__(marca, modelo, anyo)
       
        self.numPuertas = numPuertas
        
    def mostrarInfo(self):
        print(f"Vehiculo marca: {self.marca}, modelo: {self.modelo} del año {self.anyo}, con {self.numPuertas} puertas .")  

class Moto(Vehiculo):
     

    def __init__(self, marca, modelo, anyo, disenyo):

        super().__init__(marca, modelo, anyo)
       
        self.disenyo = disenyo
        
    def mostrarInfo(self):
        print(f"Vehiculo marca: {self.marca}, modelo: {self.modelo} del año {self.anyo}, con diseño {self.disenyo}  .")  

class Camion(Vehiculo):
     

    def __init__(self, marca, modelo, anyo, capCarga):

        super().__init__(marca, modelo, anyo)
       
        self.capCarga = capCarga
        
    def mostrarInfo(self):
        print(f"Vehiculo marca: {self.marca}, modelo: {self.modelo} del año {self.anyo}, con {self.capCarga} toneladas de capacidad de carga .")  




auto1 = Auto("Ferrari", "GTO", 1990, 2)
moto1 = Moto("Honda", "SevenFifty", 2000, "Naked")
camion1 = Camion("Barreiros", "H978", 1975, 3)

autosLocos =[auto1, moto1, camion1]

def esModerno(ant):
    if ant<=5:
        print("El coche es moderno")
    else:
        print("Es antiguo")   

def gestorAutos(lista):
    for l in lista:
        l.mostrarInfo()
        esModerno(l.mostrarAntiguedad())

gestorAutos(autosLocos)

@staticmethod
def comparadorEdad(vechiculo1, vehiculo2):
    dif = (abs)(vechiculo1.mostrarAntiguedad() - vehiculo2.mostrarAntiguedad())
    print(f"la Difeirencia de años son {dif}")

comparadorEdad(moto1, auto1)