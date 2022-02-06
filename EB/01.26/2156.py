# 2156. 포도주 시식

n = int(input())
w = [0] * n
dp = [0] * n

for i in range(n):

    w[i] = int(input())

for i in range(n):

    if i == 0:
        dp[i] = w[i]
    elif i == 1:
        dp[i] = w[i-1] + w[i]
    else:
        dp[i] = max(dp[i-1], dp[i-2] + w[i], dp[i-3] + w[i-1] + w[i])

print(dp[n])
