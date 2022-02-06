# 10:05 -> 10:45
# 10:45 [FAIL] - timeout
# 10:53 retry -> 11:06 [Success]
N = int(input())
A = list(map(int,input().split()))

if N == 1:
    print(1)
else:
    dp = [0]*N
    dpUp, dpDown = dp[:],dp[:]

    for i in range(N):
        cnt = 0
        for j in range(0,i):
            if A[i] > A[j]:
                cnt = max(cnt,dpUp[j])
        dpUp[i] = cnt +1
    for i in range(N-1,-1,-1):
        cnt = 0
        for j in range(N-1,i,-1):
            if A[i] > A[j]:
                cnt = max(cnt,dpDown[j])
        dpDown[i] = cnt +1
    for i in range(N):
        dp[i] = dpUp[i] + dpDown[i]-1
    print(max(dp))
