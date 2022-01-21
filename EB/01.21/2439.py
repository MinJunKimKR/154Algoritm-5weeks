# 2439. 별찍기 -2

n = int(input())

for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)
