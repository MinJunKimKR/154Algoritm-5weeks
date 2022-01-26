# 11:45 -> 12:15
from bisect import bisect_left
N = int(input())
A = list(map(int,input().split()))
INF = 1001
dp=[INF]*(N+1)
dp[0] = A[0]
if N == 1:
    print(1)
else:
    for i in range(1,N):
        idx = bisect_left(dp,A[i])
        if dp[idx] > A[i]:
            dp[idx] = A[i]            
    print(len([x for x in dp if x != INF]))
    
    # for i in range(1,N):
    #     cnt = 0
    #     for j in range(0,i):
    #         if A[i] > A[j]:
    #             cnt = max(cnt, dp[j])
    #     dp[i] = cnt+1
    # print(max(dp))
        