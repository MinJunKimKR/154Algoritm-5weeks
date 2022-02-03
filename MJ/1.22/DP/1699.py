#12:00 -> 12:30
# 12:35 [FAIL]
# 12:45 [Success]
import math
N = int(input())
if N < 4:
    print(N)
else:
    INF = 1000000
    dp=[INF]*(N+1)
    dp[0],dp[1],dp[2],dp[3] = 0,1,2,3
    for i in range(2, INF):
        num = i*i
        if num > N:
            break
        for j in range(num, N+1, 1):
            if dp[j] > 1+dp[j-num]:
                dp[j] = 1+dp[j-num]
    print(dp[N])