def division(num1, num2):
    return num1 / num2


def get_result():
    number1 = int(input('Please enter a dividend - '))
    number2 = int(input('Please enter a divisor - '))
    while number2 == 0:
        number2 = int(input("Division by 0 is not possible. Please enter a number, which is not 0 - "))
    print(f'{number1} divided by {number2} is equal to {division(number1, number2)}.')


get_result()
