# 7:05 -> 7:35
# TIMEOUT
# 7:35 -> FAIL
# 8:02 -> Success
N = int(input())

if N == 1:
    print(1)
if N == 2 :
    print(3)
if N > 2:     
    dp = [0]*(N+1)
    dp[1],dp[2] = 1,3
    for i in range(3,N+1):
        dp[i] = (dp[i-1])+(dp[i-2]*2)
    print(dp[N]%10007)


