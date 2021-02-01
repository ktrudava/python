class DivisionByZeroException(Exception):

    def __str__(self):
        return f'You cannot divide by zero!'

print('Please, Insert 2 numbers for division')
x = float(input("x: "))
y = float(input("y: "))

try:
    if y == 0:
        raise DivisionByZeroException()
    result = x / y
except DivisionByZeroException as error:
    print(error)
else:
    print(f'The result is {result}.')
