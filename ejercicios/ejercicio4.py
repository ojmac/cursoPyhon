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
       
        self.__marca = marca
        self.__modelo = modelo
        self.__anyo = anyo

    def mostrarInfo(self):
        print(f"Vehiculo marca: {self.__marca}, modelo: {self.__modelo} del año {self.__anyo}.")

  
    def mostrarAntiguedad(self):
           anio_actual = datetime.now().year
           ant = anio_actual - self.__anyo 
           print(f"La edad de este vehículo es de: {ant} ")
           return ant

    @staticmethod
    def comparadorEdad( vechiculo1, vehiculo2):
        dif = (abs)(vechiculo1.mostrarAntiguedad() - vehiculo2.mostrarAntiguedad())
        print(f"la Difeirencia de años son {dif}")

class Auto(Vehiculo):
     
    def __init__(self, marca, modelo, anyo, numPuertas):

        super().__init__(marca, modelo, anyo)
       
        self.__numPuertas = numPuertas
        
    def mostrarInfo(self):
        super().mostrarInfo()

        print(f" con {self.__numPuertas} puertas.")  

class Moto(Vehiculo):
     
    def __init__(self, marca, modelo, anyo, disenyo):

        super().__init__(marca, modelo, anyo)
       
        self.__disenyo = disenyo
        
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f" con diseño {self.__disenyo}.")  

class Camion(Vehiculo):
     

    def __init__(self, marca, modelo, anyo, capCarga):

        super().__init__(marca, modelo, anyo)
       
        self.__capCarga = capCarga
        
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f" con {self.__capCarga} toneladas de capacidad de carga.")  




auto = Auto("Ferrari", "GTO", 1990, 2)
moto = Moto("Honda", "SevenFifty", 2000, "Naked")
camion = Camion("Barreiros", "H978", 1975, 10.5)

autosLocos =[auto, moto, camion]

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

Vehiculo.comparadorEdad(moto, auto)
camion.comparadorEdad(auto, camion)