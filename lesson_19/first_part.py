# import datetime

# now = datetime.datetime.now()
# print(now)

# current_date = datetime.date.today()
# print(current_date)

# print(dir(datetime))

# d = datetime.date(2025, 1, 5)
# print(d)
# print(type(d))

# from datetime import date

# d = date(2025, 1, 5)
# print(d)

# todays_date = date.today()
# print(todays_date)

# timestamp = date.fromtimestamp(1333233323)
# print(timestamp)

# today = date.today()
# print("Year: ", today.year)
# print("Month: ", today.month)
# print("Day: ", today.day)

# from datetime import time

# a = time()
# print(a)

# b = time(11, 55, 25)
# print(b)

# c = time(hour = 11, minute = 55, second = 25)
# print(c)

# d = time(11, 55, 25, 222223)
# print(d)

# a = time(12, 2, 45, 5)
# print(a.hour)
# print(a.minute)
# print(a.second)
# print(a.microsecond)

# from datetime import datetime

# a = datetime(2025, 1, 28)
# # print(a)

# b = datetime(2025, 1, 28, 23, 24, 55, 342800)
# # print(b)

# print(b.year, b.month, b.hour, b.minute, b.timestamp())

# from datetime import datetime, date

# t1 = date(2025, 1, 12)
# t2 = date(2022, 6, 17)

# t3 = t1 - t2
# print(t3)

# t4 = datetime(2025, 1, 12, 7, 9, 33)
# t5 = datetime(2022, 6, 17, 5, 55, 13)

# t6 = t4-t5
# print(t6)

# print(type(t3))
# print(type(t6))


#from datetime import timedelta

# t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
# t2 = timedelta(days = 4, hours = 11, minutes= 4, seconds=54)
# t3 = t1 - t2
# print(t3)

# t = timedelta(days=5, hours = 1, seconds=22, microseconds=233323)
# print(t.total_seconds())

# mm/dd/yyyy dd/mm/yyyy

# from datetime import datetime

# now = datetime.now()

# t = now.strftime("%H:%M:%S")
# print(t)

# s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(s1)

# s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# print(s2)

from datetime import datetime

# date_string = "25 December, 2024"
# print(date_string)


# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print(date_object)

# import pytz
# tz_Moscow = pytz.timezone("Europe/London")
# now = datetime.now(tz_Moscow)
# print(now)


# Ввести дату через инпут в формате гггг-дд-мм
# Вывести какой это был день недели
###
# Пришельцы обещали прилететь через 4321 день, когда это случится?
###
# Найти ближайший день когда следующая пятница 13.
####
# Сколько тебе миллисекунд? Напиши программу, которая считает сколько миллисекунд прошло с твоего рождения
today = date.today()
month = today.month
year = today.year
while True:
    day_x = date(year, month, 13)
    if day_x.weekday() == 4:
        return day_x
    month+=1
    if month > 12:
        month =1
        year +=1

