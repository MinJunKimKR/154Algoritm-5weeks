# 6:43 -> 7:08
# 6:51 [FAIL] ->10007로 나머지 구하는 내용이 빠져있었음, 2미만 이면 구하는거 빠져있음
# 6:56 [SUCCESS]
N = int(input())

if N == 1:
    print(1)
else:
    dp = [0] * (N+1)

    dp[1], dp[2] = 1,2

    for i in range(3,N+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N]%10007)