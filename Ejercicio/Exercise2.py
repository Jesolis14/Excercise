x = int(input('Dáme un numero: ' ))

if x % 2 == 0 and x % 4 !=0:
    print('Tu número es par')
elif x % 4 == 0:
    print('Tu numero es par y divisible por 4')
else:
    print('Tu número es impar')

y=int(input('Damo otro número: '))
if x % y == 0:
    print(f'{x} es divisible por {y}')
elif y % x == 0:
    print(f'{y} es divisible por {x}')
else:
    print('ningún número es divisible por el otro')