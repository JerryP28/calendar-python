import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020, 11 ))

print(calendar.monthcalendar(2020, 11))

print(calendar.calendar(2020))

day_of_the_week = calendar.weekday(2020, 11, 4)
print(day_of_the_week)

is_leep = calendar.isleap(2020)
print(is_leep)

how_many_leap_days = calendar.leapdays(2000,2020)
print(how_many_leap_days)