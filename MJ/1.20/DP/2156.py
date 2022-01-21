# 1:22 -> 1:55
# 1:50 [FAIL]
# 1:57 -> 2:59

N = int(input())
wines = []
for _ in range(N):
    wines.append(int(input()))
if N < 3:
    print(sum(wines))
else:
    dp = wines[:]
    dp[1] = wines[0]+wines[1]
    dp[2] = max(wines[0]+wines[1],wines[2]+wines[0],wines[1]+wines[2])

    for i in range(3, N):
        dp[i] = max(dp[i-1], wines[i]+dp[i-2], wines[i]+wines[i-1]+dp[i-3])
    print(dp[N-1])