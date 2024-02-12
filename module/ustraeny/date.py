"""
datetime(время и дата) --> Работа с
"""
import math
# from datetime import datetime
#
# brithday = datetime(2006,5,26)
# print(brithday)




# from datetime import datetime
# now = datetime.now()
# print(now.strftime("%Y-%m-%d"))             # 2017-05-03
# print(now.strftime("%d/%m/%Y"))             # 03/05/2017
# print(now.strftime("%d/%m/%y"))             # 03/05/17
# print(now.strftime("%d %B %Y (%A)"))        # 03 May 2017 (Wednesday)
# print(now.strftime("%d/%m/%y %I:%M"))       # 03/05/17 01:36
#
# from datetime import timedelta
#
# three_hours = timedelta(hours=3)
# print(three_hours)  # 3:00:00
# three_hours_thirty_minutes = timedelta(hours=3, minutes=30)  # 3:30:00
#
# two_days = timedelta(2)  # 2 days, 0:00:00
#
# two_days_three_hours_thirty_minutes = timedelta(days=2, hours=3, minutes=30)  # 2 days, 3:30:00
#
# from datetime import timedelta, datetime
#
# now = datetime.now()
# print(now)  # 2017-05-03 17:46:44.558754
# two_days = timedelta(2)
# in_two_days = now + two_days
# print(in_two_days)  # 2017-05-05 17:46:44.558754
#
#
#
#
#
#
# from datetime import datetime
# import locale
#
# locale.setlocale(locale.LC_ALL, "")
#
# now = datetime.now()
# print(now.strftime("%d %B %Y (%A)"))  # 03 Май 2017 (среда)
#
# from datetime import timedelta, datetime
#
# now = datetime.now()
# print(now)  # 2017-05-03 17:46:44.558754
# two_days = timedelta(2)
# in_two_days = now + two_days
# print(in_two_days)  # 2017-05-05 17:46:44.558754
#
# from datetime import timedelta, datetime
#
# now = datetime.now()
# till_ten_hours_fifteen_minutes = now - timedelta(hours=10, minutes=15)
# print(till_ten_hours_fifteen_minutes)
#
# from datetime import timedelta, datetime
#
# now = datetime.now()
# twenty_two_may = datetime(2017, 5, 22)
# period = twenty_two_may - now
# print("{} дней  {} секунд   {} микросекунд".format(period.days, period.seconds, period.microseconds))
# # 18 дней  17537 секунд   72765 микросекунд
#
# print("Всего: {} секунд".format(period.total_seconds()))
# # Всего: 1572737.072765 секунд
#
#
# from datetime import datetime
#
# now = datetime.now()
# deadline = datetime(2017, 5, 22)
# if now > deadline:
#     print("Срок сдачи проекта прошел")
# elif now.day == deadline.day and now.month == deadline.month and now.year == deadline.year:
#     print("Срок сдачи проекта сегодня")
# else:
#     period = deadline - now
#     print("Осталось {} дней".format(period.days))




from datetime import datetime


def func():

    i = datetime(2006, 5, 26, 12, 0, 0)
#
    a = i.strftime("%d-%m-%y")
    b = i.strftime("%b:%M:%S")
    c = i.second
#
    print(f"День рождения: {a}")
    print(f"Час рождения: {b}")
    print(f"Секунда рождения: {c}")


func()
#
# from datetime import datetime
# now = datetime.now()
# birth = datetime(2024, 5, 26)
# res = birth - now
# years = res.days // 365
# days = res.days % 365
# second = res.seconds
# micro = res.microseconds
# minutes = second // 60
# second = second % 60
# hours = minutes // 60
# minutes = minutes % 60
#
# print(datetime)
# from datetime import datetime
#
# a = datetime.now()
# s = a.strptime("%c")
# print(a)
# print(s)


# a = 5
# b = 1
# for i in range(1, a + 1):
#     b *= i
#
# print(b)



# print(math.factorial(9))