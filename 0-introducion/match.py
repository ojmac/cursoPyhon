def http_error(status):
   match status:    
         case 400:
              return 'Bad request'
         case 404:
              return 'Not found'
         case 418:
              return "I'm a teapot"
         case 401 | 403 | 404:
                return 'Not authorized'
         case _:
              return 'Something else'   
        
print(http_error(403)) # Not authorized

point = (12, 23)
print(point[0]) # 12
point = (13, 23, 45)    
print(point[0]) # 12   
point.__add__((1, 2)) # (13, 23, 45, 1, 2)  
point.__contains__(23) # True   
print(point.__getitem__(0)) # 13

def posicion_punto(punto):
    match punto:
        case (0, 0):
            print( 'Origen')
        case (0, y):
            print(f'Eje Y: {y}') 
        case (x, 0):
            print(f'Eje X: {x}')
        case (x, y):
            print(f'X: {x}, Y: {y}')
        case _:
            raise ValueError('Punto no válido') 

posicion_punto((0, 0)) # Origen  
posicion_punto((0, 10)) # Eje Y: 10
posicion_punto((10, 0)) # Eje X: 10
posicion_punto((10, 20)) # X: 10, Y: 20
posicion_punto((10, 20, 30)) # ValueError: Punto no válido

