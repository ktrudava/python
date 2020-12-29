month_number = int(input('Please enter month number (1 to 12) - '))

while month_number < 1 or month_number > 12:
    month_number = int(input('It should be a number from 1 to 12! Enter again! - '))

# list:

seasons_list = ['Winter', 'Spring', 'Summer', 'Autumn']

if 1 <= month_number < 3 or month_number == 12:
    print(f'Month # {month_number} belongs to {seasons_list[0]}.')
if 3 <= month_number < 6:
    print(f'Month # {month_number} belongs to {seasons_list[1]}.')
if 6 <= month_number < 9:
    print(f'Month # {month_number} belongs to {seasons_list[2]}.')
if 9 <= month_number < 12:
    print(f'Month # {month_number} belongs to {seasons_list[3]}.')

# dictionary:
dict = {12: 'Winter', 1: 'Winter', 2: 'Winter',
        3: 'Spring', 4: 'Spring', 5: 'Spring',
        6: 'Summer', 7: 'Summer', 8: 'Summer',
        9: 'Autumn', 10: 'Autumn', 11: 'Autumn'}
print(f'Month # {month_number} belongs to {dict.get(month_number)}.')
