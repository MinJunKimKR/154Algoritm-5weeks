# 1:55 -> 2:25
# 1:57 [Success]
import sys
sys_input = sys.stdin.readline
N = int(input())
xy = [list(map(int, sys_input().split())) for _ in range(N)]
sorted_xy = sorted(xy, key=lambda x: (x[1], x[0]))

for xy in sorted_xy:
    print(xy[0], xy[1])
