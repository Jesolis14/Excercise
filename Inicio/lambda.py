def increment(x):
    return x + 1

increment_v2 = lambda x : x+1

result =increment(10)

print(result)

result = increment_v2(12)
print(result)

full_name = lambda name,last_name: f'Full name is {name.title()} {last_name.title()}'
text = full_name('jesús manuel','solís durán')
print(text)