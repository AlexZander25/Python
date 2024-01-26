### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Alexander", "Arce", "Alexander")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) error
# print(my_tuple[-6]) error

print(my_tuple.count("Alexander"))
print(my_tuple.index("Arce"))
print(my_tuple.index("Alexander"))

# my_tuple[1] = 1.80 error

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Andalucia"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2] error

del my_tuple
# print(my_tuple) Se puede eliminar la tupla 