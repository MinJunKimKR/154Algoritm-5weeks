# 9095. 1, 2, 3 더하기

'''
t = int(input())

for i in range(t):
    n = int(input())
    dp = [0, 1, 2, 4]
    
    for j in range(4, n+1):
        dp.append(dp[j-1] + dp[j-2] + dp[j-3])
    print(dp[n])
    dp.clear()
'''

t = int(input())

def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-1) + sol(n-2) + sol(n-3)



for i in range(t):
    n = int(input())
    print(sol(n))
