list = []
items_counter = int(input('How many items will be in your list? - '))

while items_counter > 0:
    list.append(input('Please enter your list element - '))
    items_counter -= 1

print(f'Your list is: {list}, which consists of {len(list)} elements.')

i = 0
while i+1 < len(list):
    list[i], list[i+1] = list[i+1], list[i]
    i += 2
print(f'Changed list is: {list}.')