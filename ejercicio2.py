"""Escribir un programa que reciba una cadena de caracteres,
y devuelve un diccionario con cada palabra que contiene y sus frecuencia.
Escribir otra fucnión que reciba el dicionario generado con la función anterior
y devuelva una tupla con la palabra más repetida y su frecuencia"""


def creadorDicc(cadena):
    dicionario = {}
    cadena1 = cadena.split(" ")
    for palabra in cadena1:
        veces = 0
        for p in cadena1:
            if p == palabra:
                veces+=1
        dicionario[palabra] = veces;
    
    return dicionario

cadena = "En un lugar de la Mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero adarga antigua, rocín flaco y galgo corredor"

diccionario = creadorDicc(cadena)

def contadorPalabras(dicionario):
    max = 0
    palabra = ""
    for clave, valor in dicionario.items():
        if valor > max:
            max = valor
            palabra = clave
    print ('La palabra mas repetida es ' + palabra + ' y se repite  ' +  str(max) + ' veces')        

contadorPalabras(diccionario)
