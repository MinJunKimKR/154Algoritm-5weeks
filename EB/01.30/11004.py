# 11004. k번째 수

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = sorted(a)
print(result[k-1])
