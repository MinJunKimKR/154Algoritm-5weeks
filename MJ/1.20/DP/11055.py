# 9:12 -> 9:42
# 9:23 [Success]
N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
dp[0] = A[0]

for i in range(1, N):
    maxVal = 0
    for j in range(0, i):
        if A[j]<A[i]:
            maxVal = max(maxVal, dp[j])
    dp[i] = maxVal+A[i]
    
print(max(dp))