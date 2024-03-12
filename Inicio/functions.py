### Functions ###

def my_function ():
    print('Esto es una función')

my_function ()

def sum_two_values (first_value,second_value):
    print(first_value+second_value)
    return()

first_value=int(input('Primer numero:'))
second_value=int(input('Segundo numero: '))

sum_two_values(first_value, second_value)


def sum_two_values_with_return (first_value,second_value):
    my_sum = first_value+second_value
    return my_sum

my_result = sum_two_values_with_return (first_value,second_value)
print(my_result)

def print_name (name, surname):
    print(f'{name} {surname}')

print_name('Jesús','Solís')

def print_name_with_defaullt (name, surname, alias = 'Sin alias'):
    print(f'{name} {surname} {alias}')
    
print_name_with_defaullt('Jesús','Solís')
print_name_with_defaullt('Jesús','Solís','Chuy')

def print_texts (*texts):
    for text in texts:
        print(text.upper())
        print(text.lower())

print_texts('Hola','Python','Chuy')
print_texts('Hola')

