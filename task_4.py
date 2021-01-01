def power1(x, y):
    return x ** y

def power2(x, y):
    result = 1
    counter = 0
    while y < counter:
        result = result / x
        counter -= 1
    return result

def my_func():
    num1 = float(input('Please enter a positive number - '))
    while num1 <= 0:
        num1 = float(input('This number is not positive! Please enter a positive number - '))
    num2 = int(input('Please enter a negative integer - '))
    while num2 >= 0:
        num2 = int(input('This number is not negative! Please enter a negative number - '))
    print(f'{num1} to the power of {num2} is equal to {power1(num1, num2)}.')
    print(f'{num1} to the power of {num2} is equal to {power2(num1, num2)}.')

my_func()









