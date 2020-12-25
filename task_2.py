time_seconds = int(input('Please enter time in seconds - '))
hours = time_seconds // (60 * 60)
minutes = (time_seconds % (60 * 60)) // 60
seconds = time_seconds - hours * (60 * 60) - minutes * 60

# used different types of lines formatting:

print('%d seconds is hh:mm:ss - %d:%d:%d' % (time_seconds, hours, minutes, seconds))
print('{} seconds is hh:mm:ss - {}:{}:{}'.format(time_seconds, hours, minutes, seconds))
print('{2} seconds is hh:mm:ss - {1}:{0}:{3}'.format(minutes, hours, time_seconds, seconds))
print(f'{time_seconds} seconds is hh:mm:ss - {hours}:{minutes}:{seconds}')


# in addition, if to play with the types and make double-digits hh:mm:ss:

if hours < 10:
    hrs = str('0' + str(hours))
else:
    hrs = hours
if minutes < 10:
    mins = str('0' + str(minutes))
else:
    mins = minutes
if seconds < 10:
    secs = str('0' + str(seconds))
else:
    secs = seconds
print('%d seconds is hh:mm:ss - %s:%s:%s' % (time_seconds, hrs, mins, secs))
