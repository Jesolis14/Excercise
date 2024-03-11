frase = input('Da la frase: ')

frase = frase.split()

for i in range(len(frase)):
    frase[i] = frase[i].capitalize()

frase = ' '.join(frase)

print(frase)