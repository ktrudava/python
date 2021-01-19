russian_numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
n = open('4a_file.txt', 'w')
with open('4_file.txt') as f:
    for content in f:
        if len(content.strip()) != 0:
            line = content.split()
            n.write(russian_numbers[line[0]] + ' - ' + line[2] + '\n')
n.close()
