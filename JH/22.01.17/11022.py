import sys

n = int(input())
for i in range(n):
  try:
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")
  except:
    break