myStr = "Jesús"

print("My name is " + myStr)
print(f"My name is {myStr}")
print("My name is {0}".format(myStr))

name, surname, age = 'Jesús', 'Solís', 29

print('Mi nombre es {} {} y mi edad es {}'.format(name,surname,age))
print('Mi nombre es %s %s y mi edad es %d' %(name,surname,age))
print(f'Mi nombre es {name} {surname} y mi edad es {age}')

# Desempaquetado de carcteres
lenguage = 'Python'
a, b, c, d, e, f = lenguage

print(a)
print(b)

#División

lenguge_slice = lenguage[1:3]
print(lenguge_slice)

lenguge_slice = lenguage[1:]
print(lenguge_slice)

#reverse
reversed_lenguage = lenguage[::-1]
print(reversed_lenguage)

#print(dir(myStr))

# print(myStr.upper()) #Mayusculas
# print(myStr.lower()) #Minusculas
# print(myStr.swapcase()) #Cambiar letras
# print(myStr.capitalize()) #Mayúscula la primera
# print(myStr.replace('hello', 'bye')) #reemplazar string"
# print(myStr.count(' ')) # Contar caracter

# print(myStr.startswith('hola')) # comparar el inicio
# print(myStr.startswith('hello'))

# print(myStr.endswith('world'))

# print(myStr.split('o')) #Separar en gurpos
# print(myStr.find(' ')) #Encontrar caracter

# print(len(myStr)) #Tamaño del string
# print(myStr.index('e')) #indice del caracter

# print(myStr.isnumeric()) #es númerico?
# print(myStr.isalpha()) #es alfanumerico?

# print(myStr[0])
# print(myStr[3])
# print(myStr[4])
# print(myStr[-1])
# print(myStr[-5])
