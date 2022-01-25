#1:00 -> 1:40
# [FAIL]
# 4:16 -> 4:55
# 4:25 [Success]
N = int(input())

dp = [0] * (N+1)
dp[0] = 1
if N <2:
    print(dp[N])
else:
    dp[2] = 3
    for i in range(4,N+1,2):
        dp[i] = (dp[i-2]*3)
        for k in range(i-4,-1,-2):
            dp[i] += dp[k]*2
    print(dp[N])

# if N == 0:
#     print(0)
# if N==2:
#     print(3)
# elif N == 4:
#     print(11)
# else:
#     dp=[0]*(N+1)
#     if N >1:
#         dp[2] = 3
#     if N > 3:
#         dp[4] = 11
#     for i in range(6,N+1,2):
#             dp[i] =  (dp[i-2]*3)+((dp[i-4]*2)+2)
#     print(dp[N])

