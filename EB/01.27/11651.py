# 11651. 좌표 정렬하기2

import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    [x, y] = list(map(int, input().split()))
    a.append([x, y])

result = sorted(a, key = lambda x: (x[1], x[0]))

for i in result:
    print(i[0], i[1])
