# 3:00 -> 3:30
# 3:08 [Success]
N = int(input())
w = []


for _ in range(N):
    w.append(int(input()))

if N < 3:
    print(sum(w))
else:
    dp = [0]*N
    dp[0] = w[0]
    for i in range(1,N):
        # dp[i] = max(w[i]+w[i-1]+dp[i-3], w[i]+dp[i-2])
        dp[i] = max(dp[i-1], w[i]+w[i-1]+dp[i-3], w[i]+dp[i-2])
    print(max(dp))
# 6
# 1000 
# 1000
# 1
# 1
# 1000
# 1000