def nueva_oracion(oracion):
    oracion = oracion.lower()
    letras_acentuadas = ['á','é','í','ó','ú','ü']
    letras = ['a','e','i','o','u','u']
    for i in range(len(letras_acentuadas)):
        oracion = oracion.replace(letras_acentuadas[i],letras[i])
    for letra in oracion:
        if letra not in 'zxcvbnmasdfghjklñqwertyuiop':
            oracion = oracion.replace(letra,'')
    return oracion
    
def palindromo(oracion):
    oracion_invertida = ''
    for i in range(1,len(oracion)+1):
        oracion_invertida += oracion[-i]
    print(oracion)
    print(oracion_invertida)
    if oracion == oracion_invertida:
        return True
    else:
        return False

print('Dime la oración que quieres sabes si es un palindromo o no:')
oracion = input('')

if palindromo(nueva_oracion(oracion)):
    print(f'La oración \"{oracion}\" si es un palindromo')
else:
   print(f'La oracion \"{oracion}\" no es un palindromo')