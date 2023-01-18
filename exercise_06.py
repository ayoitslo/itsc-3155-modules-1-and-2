row_num = int(input("Enter a row number from 1 to 5: "))
col_num = int(input("Enter a column number from 1 to 5: "))


zero_array  = [[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]

zero_array[row_num - 1][col_num - 1] = 1

for row in zero_array:
    for val in row:
        print(val, end=" ")
    print()

