# 1:25 -> 1:55
# 1:46 [Su ccess]
N = int(input())

mod = 10007

dp = [[0] * 10 for _ in range(N+1)]

for i in range(10):
    dp[1][i] = 1

for step in range(2, N+1):
    for i in range(10):
        for j in range(9,i-1,-1):
            dp[step][i] =dp[step][i]+ dp[step-1][j]
print(sum(dp[N])%mod)