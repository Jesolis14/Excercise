

x=int(input('Da el año que deeas saber: '))
i=0
j=1
anbi = []
print('Los siguientes años bisiestos son:')
while i<30:
    if (x+j) % 4 == 0:
        if (x+j) % 100 != 0  or (x+j) % 400 == 0:
            anbi.append(x+j)
            i+=1       
    j+=1
print(anbi)


