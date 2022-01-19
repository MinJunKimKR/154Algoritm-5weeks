'''while True:
  try:
    a, b = map(int, input().split())
    if a==0 and b ==0:
      break
    print(a+b)
  except:
    break'''

import sys

for line in sys.stdin:
  a,b =map(int, line.split())
  if a==0 and b==0:
    break
  else:
    print(a+b)

# 84 -> 72ms