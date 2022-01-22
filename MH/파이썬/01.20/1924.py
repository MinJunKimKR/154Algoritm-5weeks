# import calendar
# arrList = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
# a,b = map(int,input().split())
# Day = calendar.weekday(2007,a,b)
# print(Day)
# print(arrList[Day])
# print(calendar.calendar(2007))

Day = 0
arrList = [31,28,31,30,31,30,31,31,30,31,30,31]
weekList = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
a,b = map(int,input().split())

for i in range(a-1):
    Day = Day + arrList[i]
Day = (Day+b) % 7

print(weekList[Day-1])

