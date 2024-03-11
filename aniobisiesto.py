
x = int(input('Dime el año que deseas y te diré si es bisiesto: '))

if x % 4 == 0:
    if x % 100 != 0:
        print(f'{x} es año bisiesto.')
    elif x % 400 == 0:
        print(f'{x} es año bisiesto.')
    else:
        print(f'{x} no es año bisiesto.')
else:
    print(f'{x} no es año bisiesto.')
