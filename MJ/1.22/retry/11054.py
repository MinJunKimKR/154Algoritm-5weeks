# 11:23->11:53
# 11:43 [Success]
N = int(input())
A = list(map(int,input().split()))

if N == 1:
    print(1)
else:
    dp = [0]*N
    dpUp,dpDown = dp[:],dp[:]
    dpUp[0] =1
    dpDown[N-1] = 1
    for i in range(1,N):
        cnt = 0
        for j in range(0,i):
            if A[i]>A[j]:
               cnt = max(dpUp[j],cnt)
        dpUp[i] = cnt +1
        
    for i in range(N-1,-1,-1):
        cnt=0
        for j in range(N-1,i,-1):
            if A[i]>A[j]:
                cnt = max(dpDown[j],cnt)
        dpDown[i] = cnt +1
    
    for i in range(N):
        dp[i] = dpUp[i]+dpDown[i]-1
        
    print(max(dp))