number = int(input('Please enter a positive integer - '))
max_digit = 0

if number < 10:
    max_digit = number
else:

    while number > 10:
        integer = number // 10
        remainder = number % 10
        if remainder > max_digit:
            max_digit = remainder
        if 10 > integer > max_digit:
            max_digit = integer
        else:
            number = integer

print(f'The greatest digit in your number is {max_digit}')
