### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (29, 1.77, 'Jesús', 'Solís', 'Jesús')

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count(29))
print(my_tuple.index('Jesús'))

my_tuple = list(my_tuple)

print(type(my_tuple))
my_tuple[4] = 'Sonora'
my_tuple.insert(1, 'Azul')

print(my_tuple)
my_tuple = tuple(my_tuple)

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined
