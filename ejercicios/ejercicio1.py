"""Escribir un programa que alamecene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista 
pregunte al usuario la nota que ha sacado en cada asignatura,
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota>
donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las 
correspondientes notas introducidas por el usuario."""


asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

notas = []

for asignatura in asignaturas:
    nota = input("¿Qué nota has sacado en " + asignatura + "?")
    notas.append(nota)  

for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado " + notas[i])   



notas = []  
 
def notasAsignaturas(*asignaturas):
    for asignatura in asignaturas:
        nota = input("¿Qué nota has sacado en " + asignatura + "?") 
        notas.append(nota)  

    
notasAsignaturas("Matemáticas", "Física", "Química", "Historia", "Lengua")   

def mostrarNotas(*asignatura):
       for i in range(len(asignatura)):
            print("En " + asignatura[i] + " has sacado " + notas[i])            

mostrarNotas("Matemáticas", "Física", "Química", "Historia", "Lengua")  