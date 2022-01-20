import sys

n = int(input())
for i in range(n):
  try:
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d" %(i+1, a+b))
  except:
    break

# print format에 대해서 더 찾아보자.
# 1. "%d", %(name)
# 2. f'name is {name}'
# 3. "Hi, my name is ",name