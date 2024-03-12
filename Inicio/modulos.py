### Modulos ###

import inicio.my_module as my_module
from inicio.my_module import sum
from inicio.my_module import printValue

my_module.sum(1,3,5)
my_module.printValue('Hola Mundo')

sum(5,6,3)
printValue('Hola')

import math

x=int(math.sqrt(25))

print(x)
print(type(math.floor(3.5)))