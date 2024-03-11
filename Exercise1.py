name = input('Cuál  es tu nombre: ')
age = int(input('CUál es tu edad: '))

print('ya cumpliste años este año?')
print('1) sí')
print('2) no')
cumple = int(input(''))

if cumple == 1:
    print(f'{name} en {2124- age} cumplirás 100 años')
else:
    print(f'{name} en {2123- age} cumplirás 100 años')