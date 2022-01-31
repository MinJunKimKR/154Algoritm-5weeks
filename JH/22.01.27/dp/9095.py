t = int(input())

for j in range(t):
  n = int(input())
  dp = [0]* 12
  dp[1] = 1
  dp[2] = 2
  dp[3] = 4

  if n in [1, 2, 3]:
    print(dp[n])
  else:
    for i in range(4, n+1):
      dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])


# 배열 결과를: sum(arr[-3:]) 로 하면 가장 최근 3개를 더한다.
# python list.append를 사용하면 굳이 index 지정하지 않아도 된다.