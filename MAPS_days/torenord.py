from datetime import datetime, timedelta

def maps_days_in_2000s():
    d = datetime(2000, 1, 1)

    while d <= datetime.now():
        if sum(int(i) for i in str(d.day) + str(d.month)) == sum(int(i) for i in str(d.year)):
            yield d

        d = d + timedelta(1)

print(len(list(maps_days_in_2000s())))
