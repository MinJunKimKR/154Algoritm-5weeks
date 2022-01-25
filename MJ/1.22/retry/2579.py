# 3:56 -> 4:26
# 4:04
N = int(input())
w = [0]


for _ in range(N):
    w.append(int(input()))

if N < 3:
    print(sum(w))
else:
    dp = [0]*(N+1)
    dp[1] = w[1]
    for i in range(2,N+1):
        dp[i] = max(w[i]+w[i-1]+dp[i-3], w[i]+dp[i-2])
        # dp[i] = max(dp[i-1], w[i]+w[i-1]+dp[i-3], w[i]+dp[i-2])
    print(dp[N])