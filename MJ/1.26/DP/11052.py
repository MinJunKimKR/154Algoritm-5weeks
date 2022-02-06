# 12:04 -> 12:34
# 12:33 [GG]
# 12:40 -> 01:10
# 12:45 -> [Success]
N = int(input())
P = list(map(int, input().split()))
P = [0] +P
dp = [0]*(N+1)
dp[1] = P[1]

for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i-j]+P[j],dp[i])

print(dp[N])


# N
# 1 = p[1]
# 2 = dp[1] + p[1], p[2]
# 3 = dp[2] + p[1], dp[1] + p[2], p[3]
# 4 = dp[3] + p[1], dp[2] + p[2], dp[1] + p[3], p[4]
# DP[i] = max(DP[i-j]+P[j], DP[i]) until j ==i
