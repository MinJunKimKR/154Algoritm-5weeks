# 11650. 좌표 정렬하기

import sys
input = sys.stdin.readline


n = int(input())    # test case
a = []

for i in range(n):
    a.append(list(map(int, input().split())))
    
result = sorted(a, key = lambda x: (x[0], x[1]))

for i in result:
    print(i[0], i[1])
