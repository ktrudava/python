f = open('5_file.txt', 'w')
f.write(input('Please enter several numbers divided by space - '))
f.close()

with open('5_file.txt', 'r') as f:
    content = f.readline()
    line_list = content.split()

print(f'The sum of the numberes entered is: {sum(int(i) for i in line_list)}.')
