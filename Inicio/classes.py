### clasess ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):
        self.full_name = f'{name} {surname} ({alias})' # propiedad publico
        self.__name = name #porpiedad privada
    

    def get_name (self):
        return self.__name
    
    def walk (self):
        print(f'{self.full_name} está caminando')

my_person = Person('Jesús', 'Solís') 
print(my_person.full_name)
my_person.walk()

my_other_person = Person('Jesús', 'Solís', 'Chuy')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'Héctor de León (El loco de los perros)'
print(my_other_person.full_name)