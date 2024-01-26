### clases ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person1:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
my_person = Person1("Alexander","Arce")    
print(f"{my_person.name} {my_person.surname}")

class Person2:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{my_person.name} {my_person.surname} ({alias})" # Propiedad publica
        self.__name = name #Propiedad privada
        self.__surname = surname
        
    def get_name(self):
        return self.__name    
        
    def walk(self):
        print(f"{self.full_name} esta caminando")    

my_person1 = Person2("Alexander","Arce")    
print(my_person1.full_name)
print(my_person1.get_name())
my_person1.walk()

my_other_person = Person2("Alexander", "Arce", "Ale")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de Leon El loco de los perros"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)