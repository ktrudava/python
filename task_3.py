salaries = []

with open('3_file.txt') as f:
    for content in f:
        if len(content.strip()) != 0:
            salaries.append(content.split())

def avr(list):
    return sum(float(i) for i in list)/len(list)

print(f'People who have salary less than 20000 are: {[el[0] for el in salaries if float(el[1]) < 20000]}.')
print(f'The average salary is: {avr([el[1] for el in salaries]):.2f}')
