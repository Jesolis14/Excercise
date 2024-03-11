import random
lista = []
x=50
for i in range(x):
    lista.append(random.randrange(1000))
print(lista)
lista.sort()
print(lista[x-2])
