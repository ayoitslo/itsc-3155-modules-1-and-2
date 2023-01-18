first_list = []
second_list = []
common_list = []

i = 0

while i < 5:
    number = input('Enter a number for the first list: ')
    first_list.append(number)
    i += 1

j = 0

while j < 5:
    number = input('Enter a number for the second list: ')
    second_list.append(number)
    j += 1

k = 0

while k < 5:
    if first_list[k] in second_list:
        if first_list[k] not in common_list:
            common_list.append(first_list[k])
    k += 1

print('First List: ' + str(first_list))
print('Second List: ' + str(second_list))
print('Common List: ' + str(common_list))