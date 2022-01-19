# 4:50 -> 5:20
# 5:01 [Success]
N = int(input())

dp = [[0]*10 for _ in range(101)]
mod = 1000000000
for i in range(1,10):
    dp[1][i] = 1

for step in range(2,N+1):
    for i in range(10):
        if i ==0:
            dp[step][i] = dp[step-1][1]
            continue
        if i == 9:
            dp[step][i] = dp[step-1][8]
            continue
        dp[step][i] = dp[step-1][i-1]+dp[step-1][i+1]
        
print(sum(dp[N]) % mod)
