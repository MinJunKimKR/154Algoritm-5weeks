# 2745. 진법 변환

import sys

n, b = map(str, sys.stdin.readline().split())
b = int(b)

print(int(n, b))
