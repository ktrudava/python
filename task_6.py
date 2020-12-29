dict1 = {}
dict_main = {}
result_dict = {'name': [], 'price': [], 'quantity': [], 'country': []}
list1 = []
list2 = []
list3 = []
list4 = []

items_number = int(input('How many items will be in your list of goods? - '))

items_counter = 0
while items_counter < items_number:
    data1 = input(f"Enter item # {items_counter + 1} name (e.g. computer) - ")
    dict1['name'] = data1
    data2 = float(input(f"Enter item # {items_counter + 1} price (e.g. 200) - "))
    dict1['price'] = data2
    data3 = int(input(f"Enter item # {items_counter + 1} quantity (e.g. 5) - "))
    dict1['quantity'] = data3
    data4 = input(f"Enter item # {items_counter + 1} country of origin (e.g. China) - ")
    dict1['country'] = data4
    dict_main[items_counter + 1] = dict1
    list1.append(data1)
    list2.append(data2)
    list3.append(data3)
    list4.append(data4)
    items_counter += 1
    dict1 = {}

result_dict['name'] = list1
result_dict['price'] = list2
result_dict['quantity'] = list3
result_dict['country'] = list4

tuples_list = dict_main.items()

print('Data structure required: ')
for item in tuples_list:
    print(item)

print(f'Required dictionary: {result_dict}')
