import math
1254
x= int(input('Indica el número que quieres saber si es primo: '))
y=0
div = []

for i in range(x):
    j=i+1
    if x % j ==0:
        y=y+1
        div.append(j)

div.remove(1)
div.remove(x)
if y==2:
    print(f'{x} es un número primo')
else:
    print(f'{x} no es un número primo')
    for a in div:
        for b in div:
            if a*b == x:
                div.remove(b)
                print(f'{a}, {int(x/a)}')


