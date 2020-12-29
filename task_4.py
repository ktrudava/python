user_line = input('Please enter several words divided by space - ').split()

for index, word in enumerate(user_line):
    print(index + 1, word[:10])
