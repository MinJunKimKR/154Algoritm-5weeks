# 11:10 ->11:40
# 11:43 [TIME OUT]
N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(A[0])
else :
    dp=[0]*N
    dp[0] = A[0]
    for i in range(1,N):
        dp[i] = max(dp[i-1]+A[i], A[i])
    print(max(dp))
 