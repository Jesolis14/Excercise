from tkinter import Y

Lessx=[]
a=1

n= int(input('Primero di la cantidad de elemento que quiera tener la serie de Fibonacci: '))
if n==0:
    fibo = []
elif n == 1:
    fibo=[1]
elif n == 2:
    fibo = [1,1]
elif n > 2:
    fibo = [1,1]
    while a < (n-1):
        fibo.append(fibo[a-1]+fibo[a])
        a+=1

print(fibo)
x = int(input('Dime el valor de número: '))

for i in fibo:
    if i < x:
        Lessx.append(i)

print(Lessx)
