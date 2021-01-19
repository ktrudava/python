import re

def find_total_lessons(list):
    return sum(int(i) for i in list)

lessons_dict = {}

with open('6_file.txt') as f:
    for line in f:
        if len(line.strip()) != 0:
            line_list = line.split()
            numbers_list = re.findall(r'\d+', line)
            subject = line_list[0]
            lessons_dict.update({subject[:(len(subject) - 1)]: find_total_lessons(numbers_list)})
    print(lessons_dict)
