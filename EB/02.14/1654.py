# 1654. 랜선 자르기

import sys

k, n = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(lan)

while start <= end:
    print("start : ", start, "end : ", end)
    mid = (start + end) // 2
    print("mid : ", mid)
    lines = 0

    for i in lan:
        print("i : ", i)
        lines += i // mid
        print("lines : ", lines)

    if lines >= n:
        start = mid + 1

    else:
        end = mid - 1

print(end)
