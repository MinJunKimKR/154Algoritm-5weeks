n = int(input())

# 2. Top down: 재귀 사용 (시간 훨씬 단축: 60ms)
num = {0: 0, 1: 0}

def dp(n):
  if n in num:
    return num[n]
  num[n] = 1 + min(dp(n//2) + n%2, dp(n//3) + n%3)
  return num[n]

print(dp(n))

'''
# dp문제...... 모든 방법 탐색 중 최선의방법을 찾는다.
# 1. Bottom up 으로 풀기 + memoization 배열에 저장 (시간: 520ms)
dp = [0] * (n + 1) # 0으로 배열 초기화

for n in range(2, n+1):
  dp[n] = dp[n-1] + 1 # -1 Step을 한다고 가정

  if n%2 == 0:
    dp[n] = min(dp[n], dp[n//2]+1) #-1 step과 /2 중 적은 step저장
  if n%3 == 0:
    dp[n] = min(dp[n], dp[n//3]+1)
  
print(dp[n])'''
'''
# 완전 탐색 : 시간 에러
def checkn(n, cnt):
  if n== 1:
    return cnt
  
  cnts = []
  if n%3 == 0:
    cnts.append(checkn(n//3, cnt+1))
  if n%2 == 0:
    cnts.append(checkn(n//2, cnt+1))
  cnts.append(checkn(n-1, cnt+1))
  return min(cnts)

print(checkn(n, 0))'''