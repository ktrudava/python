from itertools import count, cycle

list1 = []

for el in count(3):
    if el > 10:
        break
    else:
        list1.append(el)

print(list1)

list2 = [1, 2, 5, 10, 45]
list3 = []
counter = 0

for num in cycle(list2):
    if counter == len(list2)*3:
        break
    else:
        list3.append(num)
        counter += 1

print(list3)



