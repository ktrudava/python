aim = float(input('What is your aim to run a day, km? - '))
day_result = float(input('How many kilometres did you run on your first day? - '))
if day_result <= 0:
    print("Sorry, with this result you won't move anywhere... Try again, when you run at least something.")

counter_days = 1
while day_result < aim:
    day_result = day_result * 1.1
    counter_days += 1

print(f'You will achieve your aim to run {aim} km a day on the day {counter_days}.')


