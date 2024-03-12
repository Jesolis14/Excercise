### Conditionals ###

for i in range(100):
    j=i+1
    if j % 3 == 0 and j % 5 != 0:
        print('Fizz')
    elif j % 3 != 0 and j % 5 == 0:
        print('Buzz')
    elif j % 3 == 0 and j % 5 == 0:
        print('FizzBuzz')
    else:
        print(j)