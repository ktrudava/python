from sys import argv
script_name, work_hours, rate_per_hour, bonus = argv

print(script_name)
print(f'The salary is: {(int(work_hours) * float(rate_per_hour)) + float(bonus)}')
