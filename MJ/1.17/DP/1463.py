# 6:35 -> 7:00
# 6:41 [success]


N = int(input())
INF = int(1e7)
dp = [INF]* (N+1)
dp[N] = 0
while N > 1:
    if N%3 == 0:
        dp[N//3] = min(dp[N//3],dp[N]+1)
    if N%2 == 0:
        dp[N//2] = min(dp[N//2],dp[N]+1)
    dp[N-1] = min(dp[N-1],dp[N]+1)
    N -=1
print(dp[1])
    
