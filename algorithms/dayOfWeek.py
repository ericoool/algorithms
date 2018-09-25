# dayOfWeek.py
'''
末日算法，平年2曰28日设置为“末日”，闰年是2曰29日。
末日的星期每跨一年加1，遇闰年加2。
年份被100整除，但不能被400整除，不是闰年
'''

# 已知20180228是星期3
# 已知公元1年0228是星期3
# 已知19000228是星期3
endDay = 3
endDayOfWeek2018 = 3


# 用户输入
def user_input():
    global year
    year = int(input("输入需要查询的年份(如：2018)："))
    global day
    day = input("输入日期(如：0916):")
    return year, day


# 判断每年末日是星期几
'''
for i in range(0,3000):
    if i%100 == 0 and i%400 != 0:
        print(i)
'''

def end_day(year):
    global endDay
    endDay = (endDay + abs(year - 1900) + abs(year - 1900) // 4) % 7
    # print("endDay: {}".format(endDay))
    return endDay

# 判断是否闰年
def leap_year(year):
    if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
        print("{0}是闰年".format(year))
    elif year % 100 == 0 and year % 400 != 0:
        print("{0}是平年".format(year))
    elif year % 4 != 0:
        print("{0}是平年".format(year))
    else:
        return None


# 知道末日星期，找到输入day是星期几
def day_of_week(day):
    if day[0:2] == "03":
        dayOfWeek = (int(day[-2:]) % 7 + endDay) % 7
        print("{0}{1}是星期{2}".format(year, day, dayOfWeek))
    elif day[0:2] == "04":
        dayOfWeek = (int(day[-2:]) % 7 + endDay + 31) % 7
        print("{0}{1}是星期{2}".format(year, day, dayOfWeek))
    elif day[0:2] == "05":
        dayOfWeek = (int(day[-2:]) % 7 + endDay + 61) % 7
        print("{0}{1}是星期{2}".format(year, day, dayOfWeek))
    elif day[0:2] == "06":
        dayOfWeek = (int(day[-2:]) % 7 + endDay + 92) % 7
        print("{0}{1}是星期{2}".format(year, day, dayOfWeek))
    elif day[0:2] == "07":
        dayOfWeek = (int(day[-2:]) % 7 + endDay + 122) % 7
        print("{0}{1}是星期{2}".format(year, day, dayOfWeek))
    elif day[0:2] == "08":
        dayOfWeek = (int(day[-2:]) % 7 + endDay + 153) % 7
        print("{0}{1}是星期{2}".format(year, day, dayOfWeek))
    elif day[0:2] == "09":
        dayOfWeek = (int(day[-2:]) % 7 + endDay + 184) % 7
        print("{0}{1}是星期{2}".format(year, day, dayOfWeek))
    elif day[0:2] == "10":
        dayOfWeek = (int(day[-2:]) % 7 + endDay + 214) % 7
        print("{0}{1}是星期{2}".format(year, day, dayOfWeek))
    elif day[0:2] == "11":
        dayOfWeek = (int(day[-2:]) % 7 + endDay + 245) % 7
        print("{0}{1}是星期{2}".format(year, day, dayOfWeek))
    elif day[0:2] == "12":
        dayOfWeek = (int(day[-2:]) % 7 + endDay + 275) % 7
        print("{0}{1}是星期{2}".format(year, day, dayOfWeek))
    elif day[0:2] == "01":
        dayOfWeek = (int(day[-2:]) % 7 + endDay + 306) % 7
        print("{0}{1}是星期{2}".format(year, day, dayOfWeek))
    elif day[0:2] == "02":
        dayOfWeek = (int(day[-2:]) % 7 + endDay + 337) % 7
        print("{0}{1}是星期{2}".format(year, day, dayOfWeek))
    else:
        return None


def start():
    user_input()
    end_day(year)
    leap_year(year)
    day_of_week(day)


start()
