def parameters(**kwargs):
    string = ''
    for key, value in kwargs.items():
        string += value + ' '
    return string

def my_func():
    name = input('Please enter your name - ')
    second_name = input('Please enter your second name - ')
    birth_year = input('Please enter your birth year - ')
    city = input('Please enter the city you live in - ')
    email = input('Please enter your email - ')
    phone = input('Please enter your phone number - ')
    result = parameters(name=name, second_name=second_name, birth_year=birth_year, city=city, email=email, phone=phone)
    print(f'{result}')
my_func()