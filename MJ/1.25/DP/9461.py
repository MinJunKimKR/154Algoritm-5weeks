#4:35 -> 5:05
# 5:00 -> [FAIL]
# 5:03 [Success]
T = int(input())
dp = [0,1,1,1,2,2]
result = []
for _ in range(T):
    N = int(input())
    if N < 6:
        result.append(dp[N])
        continue
    dp = dp + ([0]*(N-5))
    for i in range(6,N+1):
        dp[i] = dp[i-1] + dp[i-5]
    result.append(dp[N])
for dp in result:
    print(dp)