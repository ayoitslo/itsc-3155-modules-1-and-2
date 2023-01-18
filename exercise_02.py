string_1 = input('Enter a string: ')
string_2 = input('Enter another string: ')

if string_1.endswith(string_2):
    print('True')

elif string_2.endswith(string_1):
    print ('True')

else:
    print('False')