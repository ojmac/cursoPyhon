import itertools    

lista_marcas = ['Audi', 'BMW', 'Mercedes', 'Volkswagen', 'Porsche'] 
lista_anyos = [2010, 2011, 2012, 2013, 2014]

marca_anios =list(itertools.product(lista_marcas, lista_anyos)) 

print(marca_anios)  # [('Audi', 2010), ('Audi', 2011), ('Audi', 2012), ('Audi', 2013), ('Audi', 2014), ('BMW', 2010), ('BMW', 2011), ('BMW', 2012), ('BMW', 2013), ('BMW', 2014), ('Mercedes', 2010), ('Mercedes', 2011), ('Mercedes', 2012), ('Mercedes', 2013), ('Mercedes', 2014), ('Volkswagen', 2010), ('Volkswagen', 2011), ('Volkswagen', 2012), ('Volkswagen', 2013), ('Volkswagen', 2014), ('Porsche', 2010), ('Porsche', 2011), ('Porsche', 2012), ('Porsche', 2013), ('Porsche', 2014)]  




"""
for marca in lista_marcas:
    for anyo in lista_anyos:
        marca_anios.append((marca, anyo))   

print(marca_anios)  # [('Audi', 2010), ('Audi', 2011), ('Audi', 2012), ('Audi', 2013), ('Audi', 2014), ('BMW', 2010), ('BMW', 2011), ('BMW', 2012), ('BMW', 2013), ('BMW', 2014), ('Mercedes', 2010), ('Mercedes', 2011), ('Mercedes', 2012), ('Mercedes', 2013), ('Mercedes', 2014), ('Volkswagen', 2010), ('Volkswagen', 2011), ('Volkswagen', 2012), ('Volkswagen', 2013), ('Volkswagen', 2014), ('Porsche', 2010), ('Porsche', 2011), ('Porsche', 2012), ('Porsche', 2013), ('Porsche', 2014)]         
   """

