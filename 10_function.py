### Funciones ###

def my_function():
    print("Esto es una funcion")
    
my_function()    
my_function()    
my_function()

def sum_two_values(n1, n2):
    print(n1 + n2)
    
sum_two_values(5, 7)        
sum_two_values(55416, 71231)        
sum_two_values("5", "4")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(n1, n2):
    my_sum = n1 + n2
    return my_sum

result = sum_two_values_with_return(10, 5)
print(result)

def print_name(name, surname):
    print(f"{name} {surname}")
    
print_name(name = "Alexander", surname = "Arce")    

def print_name_with_defaul(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
    
print_name_with_defaul("Alexander","Arce", "ale")    
print_name_with_defaul("Alexander","Arce")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
    
print_upper_texts("Hola", "Python", "Ale")    
print_upper_texts("Hola")    
