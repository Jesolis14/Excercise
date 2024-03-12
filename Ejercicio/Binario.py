# Programa que tranformas número binarios en decimales y vuseversa
def a_decimal():
    count = 0
    num = input('Da el número en binario que desees cambiarlo a decimal.')
    if num.count('1') + num.count('0')  != len(num):
        return 'El numero que diste no es binario.'
    else:
        for i in range(len(num)):
            count += int(num[-i-1]) * (2**i)
    return f'El número {num} en decimal es {count}'


def a_binario():
    n = 0
    binario = 0
    num_1 = input('Da el número en decimal que desees cambiarlo a binario.')
    num = num_1
    try:
        num = int(num)
        while 2**n <= num:
            n += 1
        n = n-1
        for i in range(-n,1):
            if num >= (2**(-i)):
                binario += 10**(-i)
                num = num - (2**(-i))
        return f'El número {num_1} en binario es {binario}'

    except:
        return 'Eso no es un número decimal.'

print('Qué deseas hacer?:')
print('1) tranformar decimal a binario.')
select = int(input('2) transformar binario a decimal.'))

if select == 1:
    print(a_binario())
elif select == 2:
    print(a_decimal())
else:
    print('El número seleccionado no es válido.')

