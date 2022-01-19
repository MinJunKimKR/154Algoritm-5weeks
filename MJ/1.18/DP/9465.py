# 12:50 -> 1:20
# 1:26 [TIMEOUT]
# 1:39 [RUNTIME]
# 1:48 [SUCCESS]
T = int(input())

for _ in range(T):
    n = int(input())
    dp = [[0] * n for _ in range(2)]
    stickers = []
    stickers.append(list(map(int,input().split())))
    stickers.append(list(map(int,input().split())))
    if n ==1:
        print(max(stickers[0][0],stickers[1][0]))
        continue
    dp[0][0], dp[1][0],dp[0][1], dp[1][1]  = stickers[0][0],stickers[1][0], stickers[0][1]+stickers[1][0],stickers[1][1]+stickers[0][0]
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + stickers[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + stickers[1][i]
    print(max(dp[0][n-1],dp[1][n-1]))
    

# 2
# 1
# 10
# 15
# 2
# 10 10
# 20 30