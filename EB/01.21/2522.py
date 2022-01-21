# 2522. 별찍기 -12

n = int(input())

for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)
for i in range(1, n):
    print(' ' * i + '*' * (n-i))
    
