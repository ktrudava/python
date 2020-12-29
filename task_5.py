rating = [7, 5, 3, 3, 2]

new_number = int(input('Enter a new number for the list - '))

for item, number in enumerate(rating):
    if new_number > number:
        rating.insert(item, new_number)
        break
    elif new_number <= rating[-1]:
        rating.append(new_number)
        break
print(rating)
