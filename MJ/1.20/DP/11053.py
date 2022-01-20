# 3:45 -> 4:15

from bisect import bisect_left
N = int(input())
A = list(map(int,input().split()))
INF = 1001
if N == 1:
    print(1)
else:
    dp = [INF]*N
    dp[0] = A[0]
    
    for i in range(1,N):
        idx = bisect_left(dp,A[i])
        if dp[idx] > A[i] or dp[idx] == 0:
            dp[idx] = A[i]
    print(len([x for x in dp if x != INF]))
            
    
# N = int(input())
# A = list(map(int,input().split()))

# if N == 1:
#     print(1)
# else:
#     dp = [0]*N
#     dp[0] = 1
#     for i in range(1, N):
#         cnt = 0
#         for j in range(i):
#             if A[j]<A[i]:
#                 if dp[j] > cnt:
#                     cnt = dp[j]
#         dp[i] = cnt+1
#     print(max(dp))