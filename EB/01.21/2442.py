# 2442. 별찍기 -5

n = int(input())

for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
        
