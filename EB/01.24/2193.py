# 2193. 이친수

n = int(input())
dp = [0] * (n+1)

for i in range(n+1):

    if i == 1:
        dp[i] = 1
    else:
        dp[i] = dp[i-1]+dp[i-2]

print(dp[n])
