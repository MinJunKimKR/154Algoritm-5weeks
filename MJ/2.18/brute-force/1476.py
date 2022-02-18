# 12:36-> 1:06
# 12:36 [success]
ESM = list(map(int, input().split()))

days = [1, 1, 1]
max_days = [15, 28, 19]

year = 1
while days != ESM:
    year += 1
    days = list(map(lambda x: x+1, days))
    for i in range(3):
        if days[i] > max_days[i]:
            days[i] = days[i] % max_days[i]
print(year)
