from math import factorial

number = int(input('Please enter an integer - '))

def create_gen(number):
    gen = range(1, number + 1)
    for i in gen:
        yield i

product = 1

for el in create_gen(number):
    product = product * el
    print(product)

# for check:
print(factorial(number))
