# 9:20 -> 9:50
# 9:35 [Success]
# 9:37 -> 10:02 [Success]
N = int(input())
A = list(map(int,input().split()))
INF = 1001
dp = []
dp.append(A[0])
for i in range(1,N):
    idx = 0
    for dpVal in dp : 
        if dpVal > A[i]:
            idx +=1
    if idx > len(dp)-1:
        dp.append(A[i])
        continue
    dp[idx] = A[i]
    
print(len(dp))
# dp[0] = 1


# for i in range(1, N):
#     cnt = 0
#     for j in range(0,i):
#         if A[j]>A[i]:
#             cnt = max(dp[j], cnt)
#     dp[i] = cnt+1
# print(max(dp))

5