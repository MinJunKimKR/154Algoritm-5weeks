# 2446. 별찍기 -9

n= int(input())

for i in range(n):
    print(' ' * i + '*' * ((n-i)*2-1))
for i in range(2, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
