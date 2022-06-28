from datetime import datetime, timedelta

# there is a unix time stamp, you can check it up unit Epoch.
time_1 = datetime.now()
time_2 = datetime(2021, 5, 27)
diff = time_1 - time_2

t = timedelta(weeks=1)

print(time_1)
print(time_1.day)
print(time_1.month)
print(time_1.year)
print(time_1.hour)
print(time_1.minute)
print(time_1.second)
print(type(diff))
print(diff)
print(time_1 + t)

date_from_str = datetime.strptime("2022-02-02", "%Y-%m-%d")
date_from_str_1 = datetime.strptime("03/2022/02", "%m/%Y/%d")
date_from_str_2 = datetime.strptime("03/22/02", "%m/%y/%d")  # Whenever you use short year format, you represent small y
print(date_from_str)
print(date_from_str.year)
print(date_from_str_1)
print(date_from_str_2)
# %A is for day, %d for day, %B for month, %Y for year
print(time_1.strftime("%A"))
print(time_1.strftime("%A %d, %B %Y"))

