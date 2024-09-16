def numbers_sum(x):
    sum = 0
    counter = True
    for number in x:
        if number.isdigit():
            sum += float(number)
        else:
            counter = False
            break
    return sum, counter

def my_func():
    sum = 0
    while True:
        list = input('Please enter several numbers divided by space - ').split()
        result = numbers_sum(list)
        sum += result[0]
        print(f'The sum of everything is: {sum}')
        if not result[1]:
            break

my_func()
