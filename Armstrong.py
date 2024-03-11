def armstrong (num):
    verdad = True
    i = 0
    sum = 0
    while sum < num:
        sum = 0
        for a in str(num):
            a=int(a)
            sum = a**i + sum
        i += 1
    if num < sum:
        verdad = False
    return verdad


num = int(input('Escribe el numero que deseas saber si es de Armstrong: '))
if armstrong(num) == True:
    print(f'{num} Si es un numero de Armstrong.')
else:
    print(f'{num} No es un numero de Armstrong.')


