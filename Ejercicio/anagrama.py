def anagrama (palabra1,palabra2):
    ana = True
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    if len(palabra1) != len(palabra2):
        ana= False
    else:
        lista1 = list(palabra1)
        lista2 = list(palabra2)
        for a in lista1:
            lista2.remove(a)
        if len(lista2) == 0:
            ana= True
        else:
            ana= False
    return ana

palabra1 = input('Cual va a ser tu primer palabra: ')
palabra2 = input('Cual va a ser la segunda palabra: ')

anagrama(palabra1,palabra2)

esono = anagrama(palabra1,palabra2)

if esono == True:
    print(f'{palabra1.capitalize()} y {palabra2} son anagramas')
else:
    print(f'{palabra1.capitalize()} y {palabra2} no son anagramas')
