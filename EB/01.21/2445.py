# 2522. 별찍기 -6

n = int(input())

for i in range(1, n+1):
    print('*' * i + ' ' * (n-i) + ' ' * (n-i) + '*' * i)
    
for i in range(1, n+1):
    print('*' * (n-i) + ' ' * i + ' ' * i + '*' * (n-i))
