import sys

n = int(input())
for i in range(n):
  a, b = map(int, sys.stdin.readline().split())
  print(a+b)
  
# 여러 줄 입력 받는 경우 input() -> 시간초과 
# sys.stdin.readline(): 한 줄 단위로 입력 (\n포함)
# 문자열 형태로 저장
