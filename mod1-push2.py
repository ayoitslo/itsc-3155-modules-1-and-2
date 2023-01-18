upper = ''
lower = ''

data = input('Enter a string: ')

data = data.replace(' ', '')

i = 0 

for item in data:
    if item.isupper():
       upper += item
    else:
        lower += item

sort_string = lower + upper

print(sort_string)