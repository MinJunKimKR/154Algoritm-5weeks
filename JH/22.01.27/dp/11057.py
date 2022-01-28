# 단순히 오름차순 순열 문제라고 생각했는데
# 보통 n=3으로 표를 그려보면 규칙을 찾을 수 있다.
# n=1부터 n=2, 3,까지 순차적으로 이전 값을 더한 값이 경우의 수가 된다.

n = int(input())
dp = [1]*10

MOD = 10007

for i in range(2, n+1):
  for j in range(1, 10):
    dp[j] += dp[j-1]

print(sum(dp) % MOD)