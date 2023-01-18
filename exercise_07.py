original_list = []
even_list = []
data = 0

while data != 'QUIT':
    data = input('Enter a number or QUIT to quit: ')
    if data != 'QUIT':
        original_list.append(data)
        if (int(data) % 2) == 0:
            even_list.append(data)

print('All Nums: ' + str(original_list))
print('Even Nums'+ str(even_list))