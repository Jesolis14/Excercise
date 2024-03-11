def factorial(num):
    fac=1
    for i in range(num):
        fac = fac * (i+1)
    return fac

num = int(input('A cual número quiere car el factorial: '))

factorial(num)

print(f'El factorial de {num} es {factorial(num)}.')



