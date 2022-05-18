# https://blog.csdn.net/ProQianXiao/article/details/113481092

from enum import Enum


class Weekday(Enum):
    monday = 1
    tuesday = 2
    wednesday = 3
    thirsday = 4
    friday = 5
    saturday = 6
    sunday = 7


Weekday.wednesday.label = "星期三"
Weekday.wednesday.work = "完成假期作业"
Weekday.wednesday.time = 10

for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)
print(Weekday.wednesday.label)  # 星期三
print(Weekday.wednesday.work)  # 完成假期作业
print(Weekday["friday"].value)
print(Weekday["friday"].name)
print(Weekday(1))
print(type(Weekday(1)))


# 如果想让value也不相同的话，可以导入unique

from enum import Enum, unique


@unique
class Weekday(Enum):
    monday = 1
    tuesday = 2
    wednesday = 3
    thirsday = 4
    friday = 5
    saturday = 6
    sunday = 7
    test = 3


print(Weekday.test.value)