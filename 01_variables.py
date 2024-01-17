# Variables 

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_variable = str(my_int_variable)
print(my_int_to_variable)
print(type(my_int_to_variable))

my_bool_variable = False
print(my_bool_variable)

# concatenacion de variables en un print
print(my_string_variable, my_int_to_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# variables en una sola linea. No es recomendada esta sintaxis!
name, surname, alias, age = "Alexander", "Arce", "ale", 35
print("Me llamo:", name, surname, "Mi edad es:", age, "Y mi alias es:", alias)

# inputs
name = input("Cual es tu nombre?")
age = input("Cuantos años tienes?")

print(name)
print(age)

# Cambiamos su tipo
name = 35
age = "Alexander"
print(name)
print(age)

# Forzamos el tipo?
address: str = "Mi direccion"
address = 32
print(age)