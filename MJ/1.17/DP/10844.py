# 12:16 -> 12:46
# 12:52 [FAIL]
# 1:00 [Retry] -> 1:17 [Success]
N = int(input())

mod = 1000000000

dp = [[0] *10 for _ in range(N+1)]  

for i in range(1,10):
    dp[1][i] = 1
    
for step in range(2,len(dp)):
    for i in range(10):
        if i ==0 :
            dp[step][i] = dp[step-1][i+1]
            continue
        if i ==9 :
            dp[step][i] = dp[step-1][i-1]
            continue
        dp[step][i] = dp[step-1][i-1] + dp[step-1][i+1]
print(sum(dp[N]) %mod)