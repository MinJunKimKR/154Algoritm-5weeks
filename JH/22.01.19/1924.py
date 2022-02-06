import sys
x, y = map(int, sys.stdin.readline().split())

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total_day = y
for i in range(x-1):
  total_day = total_day + dates[i]
print(days[total_day%7])


# 날짜를 리스트로 저장하여 for문 사용하여 더한다.
# switch문 대체 : if-else 문 / dictionary  사용

#calendar 모듈 사용: calendar.weekday(2007, x, y)