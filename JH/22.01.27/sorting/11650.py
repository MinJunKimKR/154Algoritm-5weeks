import sys

n = int(sys.stdin.readline())

ls = []
for i in range(n):
  [x, y] = map(int, sys.stdin.readline().split())
  ls.append([x, y])
ls.sort()

for i in range(n):
  print(ls[i][0], ls[i][1])


# 파이썬 내장라이브러리 sort()를 사용
# 리스트 두 개가 아닌 이중리스트를 사용하고, 이중리슽로 입력을 받아서 정렬했다.