from datetime import date, timedelta as td

start_date = date(2000, 1, 1) # format is year, month, day
end_date = date(2017, 3, 9)

number_of_days = end_date - start_date

MAPS_days = 0

def sum_digits(i):
    return sum(int(d) for d in str(i))

for i in range(number_of_days.days + 1):
    today = start_date + td(days=i)
    year_sum = sum_digits(today.year)
    day_month_sum = sum_digits(today.day) + sum_digits(today.month)
    if year_sum == day_month_sum:
        MAPS_days += 1

print MAPS_days