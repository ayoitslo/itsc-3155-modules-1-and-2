num_input = float(input('Enter a number: '))

i = float(num_input)
j = 1
total = float(0)

while(i != 0):
    total += float(input('Enter number ' + str(j) + ': '))
    j += 1
    i -= 1

average = float(total) / num_input; 
print('Average: ' + str(average))
