# dp는 점화식을 찾는 문제이다. 시간 투자!!
# 사각형을 쪼개는 경우의 수는 항상 같으므로 이전 값을 더해줌

n = int(input())
num = [0] * (n+1)
if n<=3:
  print(n)
else:
  num[1] = 1
  num[2] = 2

  for i in range(3, n+1):
    num[i] = num[i-2] + num[i-1]

  print(num[n]%10007)
