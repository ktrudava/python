my_list = ['Max', 32, {'year': 2000, 'month': 2}, True, 2.5, {7, 'moon', False}]

my_list.append('11000$')
print(my_list)

for item in my_list:
    print(f'Element {item} has type {type(item)}')
