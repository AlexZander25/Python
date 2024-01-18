### Strings ###


my_string = "Mi string"
my_other_string = "Mi other string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string \n escapado"
print(my_scape_string)

# Formateo

name = "Alexander"
surname = "Arce"
age = 35

print("Mi nombre {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre {name} {surname} y mi edad es {age}")

# desempaquetado de caracteres

languaje = "python"
a, b, c, d, e, f = languaje
print(a)
print(e)

# División

languaje_slace = languaje[1:3]
print(languaje_slace)

languaje_slace = languaje[1:]
print(languaje_slace)

languaje_slace = languaje[-2]
print(languaje_slace)

languaje_slace = languaje[0:6:2]
print(languaje_slace)


# reverse

reversed_languaje = languaje[::-1]
print(reversed_languaje)

# Funciones

print(languaje.capitalize())
print(languaje.upper())
print(languaje.count("t"))
print(languaje.isnumeric())
print("1".isnumeric())
print(languaje.lower())
print(languaje.upper().isupper())
print(languaje.startswith("py"))
