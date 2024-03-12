### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicielmente es un diccionario

my_other_set ={'Jesús', 'Solís', 29}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('Chihuahua')
print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add('Chihuahua')
print(my_other_set) # un set no admite repetidos

print('Solís' in  my_other_set)
print('Solis' in my_other_set)

my_other_set.remove('Solís')
print(my_other_set)

my_other_set.clear()
print(my_other_set)

print(len(my_other_set))

my_set  ={'Jesús', 'Solís', 29}

my_list = list(my_set)

print(my_list[0])

my_other_set  ={'Analisis', 'Topologia', 'EDP', 'Solís'}

my_new_set = my_set.union(my_other_set)

print(my_new_set.union({'Probabilidad'}))

print(my_new_set.difference(my_set))

print(my_set.intersection(my_other_set))

print(my_set.isdisjoint(my_other_set))