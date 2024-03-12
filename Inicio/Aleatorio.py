import random

rand = []
randless= []
randmore = [] 
n = int(input('Cuántos elementos deseas en el conjunto?: '))

i=0
while i < n:
    rand.append(random.randrange(1,1000))
    i += 1
print(rand)

num =int(input('Cuál es el número que lo ca a dividir: '))

for a in rand:
    if a <= num:
        randless.append(a)
    else:
        randmore.append(a)

print(f'Los numeros menores que {num} son: ')
print(randless)
print(f'Los numeros que son mayores que {num} son:')
print(randmore)