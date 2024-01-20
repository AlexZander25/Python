### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Alexander", "Arce", 26}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Ale")

print(my_other_set) # un set no es una estructura ordenada

my_other_set.add("Ale") # Un set no admite repetidos

print(my_other_set)

print("Ale" in my_other_set)
print("Ali" in my_other_set)

my_other_set.remove("Ale")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) ya no existe este set debido al del

my_set = {"Alexander", "Arce", 26}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))