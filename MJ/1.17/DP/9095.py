# 11:05 -> 11:35
# TIMEOUT -> 11:57
# 해설 확인
# 12:00->12:05
T = int(input())

dp = [0] * 12
dp[1],dp[2],dp[3] = 1,2,4

for i in range(4,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])