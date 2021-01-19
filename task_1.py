f = open('1_file.txt', 'w')
print('Please enter some lines and hit Enter. If you want to quit, hit Enter without entering anything. - ')

while True:
    string = input()
    if not string:
        break
    f.write(string + '\n')

f.close()
