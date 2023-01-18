original_list = []
appear_once_list = []

i = 1

while i <= 10:
    data = input('Enter number ' + str(i) + ': ')
    original_list.append(data)
    i += 1

j = 0   

while j < 10: 
    count = original_list.count(original_list[j])
    if count == 1:
        appear_once_list.append(original_list[j])
    j += 1

print('Original List: ' + str(original_list))
print('Nums that appear once: ' + str(appear_once_list))