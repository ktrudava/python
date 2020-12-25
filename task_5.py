revenue = int(input('Please enter your company revenue, USD - '))
expense = int(input('Please enter your company expense, USD - '))
if revenue > expense:
    profit = revenue - expense
    profit_rate = profit / revenue * 100
    print(f'Congratulations! Your company is profitable. The profit rate is {profit_rate:.1f} %.')
    employees = int(input('How many employees does your company have? - '))
    while employees <= 0:
        employees = int(input('Are you sure? There must be at least one - you! Think again, how many? - '))
    profit_per_employee = profit / employees
    print(f'So, the profit per employee is {profit_per_employee:.2f} USD. Not bad! For sure, you can better!')
else:
    print('Sorry! Your company is not profitable! Keep working and you will succeed!')
