import datetime

nowTime = datetime.datetime.now() # Zamane hal ro neshon mide
print(nowTime)

nowYear = nowTime.year
print(nowTime)
print(nowYear)
print(nowTime.strftime("%A")) # name of weekday.
print(nowTime.strftime("%B")) # name of month
# ************************************************

# Creating Date Objects:
date = datetime.datetime(2020, 8, 22)
print(date)
