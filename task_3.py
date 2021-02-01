class WrongTypeException(Exception):

    def __str__(self):
        return f'Wrong type'

numbers = []

print('Insert several integers please. If you think you entered enough, type "stop"!')
while True:
    s = input("num: ")
    if s == 'stop':
        break
    else:
        try:
            if not s.isdigit():
                raise WrongTypeException
            numbers.append(int(s))
        except WrongTypeException:
            print(f'Not an integer!')
print(numbers)
