import datetime

now=datetime.datetime.now()
# print(now)
# print(now.day)
# print(now.month)
# print(now.year)
# print(now.hour)
# print(now.minute)

# print(f"{now.day} - {now.month} - {now.year}")
# print(f"{now.hour} : {now .minute} : {now.second}")
# print(now.strftime("%d / %m / %y"))
print(now.strftime("%H : %M : %S"))
