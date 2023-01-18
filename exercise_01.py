number_grade = input ('Enter a grade from 0 to 100: ')

number_grade = int(number_grade)

if number_grade >= 90 and number_grade <= 100:
    print('Your grade is A')

if number_grade >= 80 and number_grade < 90:
    print('Your grade is B')

if number_grade >= 70 and number_grade < 80:
    print('Your grade is C')

if number_grade >= 60 and number_grade < 70:
    print('Your grade is D')

if number_grade < 60:
    print('Your grade is F')