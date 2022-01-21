# 2441. 별찍기 -4

n = int(input())

for i in range(n):
    print(' ' * i + '*' * (n-i))
