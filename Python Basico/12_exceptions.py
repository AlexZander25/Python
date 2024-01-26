### Exception Handling ###

n1 = 5 
n2 = 1
n2 = "1"

#try, except

try:
    print(n1 + n2)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")    
    
# try, except, else, finally

try:
    print(n1 + n2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error") 
else: # Opcional
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")       
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecucion continua")   
    
# Excepciones por tipo

try:
    print(n1 + n2)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un TypeError")        
except ValueError:
    print("Se ha producido un ValueError")    
    
# Captura de la informacion de la excepcion
    
try:
    print(n1 + n2)
    print("No se ha producido un error")     
except ValueError as error:
    print(error)        
except Exception as error:
    print(error)            