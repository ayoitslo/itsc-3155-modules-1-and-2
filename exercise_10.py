data = input('Enter a string: ')

data = data.replace(' ', '')

split_chars = list(data)
split_list = []

for i in range(0, len(split_chars), 3):
    split_list.append(split_chars[i:i+3])

print(split_list)
