lines_count = 0

with open('2_file.txt') as f:
    for line in f:
        lines_count += 1
        words_number = len(line.split())
        print(f'Line # {lines_count} has {words_number} words.')
    print(f'There are a total of {lines_count} lines in this file.')
