### Loops ###

# While

my_condition =+ 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condicion es mayor o igual que 10")    
    
print("La ejecucion continua")       

while my_condition < 20: 
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion") 
        break           
    print(my_condition)    
    
print("La ejecucion continua") 

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)
    
my_tuple = (35, 1.77, "Alexander", "Arce", "Alexander")

for element in my_tuple:
    print(element)

my_other_set = {"Alexander", "Arce", 26}   

for element in my_other_set:
    print(element) 

my_other_dict = {"Nombre":"Alexander", "Apellido":"Arce", "Edad":35, 1:"Python"}

my_other_dict = {"Nombre":"Alexander", "Apellido":"Arce", "Edad":35, 1:"Python"}

for element in my_other_dict.values():
    print(element)   


for element in my_other_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")     
    
print("La ejecucion continua")     
    
for element in my_other_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")         
