word_list = []
string = ''
i = 0

while i < 5:
    data = input('Enter a word: ')
    word_list.append(data)
    string += data + ' '
    i += 1

print('Words: ' + str(word_list))
print('One String: ' + string)