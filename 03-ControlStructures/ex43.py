
print('Enter time in 24 hour format: ')
time_24_hour = input()

hours, minutes = map(int, time_24_hour.split(':'))

if 0 <= hours < 12:
        period = "AM"
        if hours == 0:
            hours = 12 
else:
        period = "PM"
        if hours > 12:
            hours -= 12  


time_12_hour = f"{hours:02d}:{minutes:02d} {period}"

print(time_12_hour)


