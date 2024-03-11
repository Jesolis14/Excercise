### Fibonacci ###
x = int(input('Cuál número en la sucesión de Fibonacci quieres saber: '))

y_1=1
if x==1 or x==2:
    print(f'El 1 es el número en la posición {x}, en la suceesión de Fibonacci')
elif x > 0:
    y=1
    for i in range(x-2):
        y_2=y
        y=y+y_1
        y_1=y_2
    print(f'El número de Fibonacci en la posición {x} es {y}.')
else:
    print('Ese número no existe')

cadena = 'Hola Mundo'
lista = [cadena.split()]
print(lista)