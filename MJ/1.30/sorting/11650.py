# 1:50 -> 2:20
# 1:53 [SUCCESS]
import sys
sys_input = sys.stdin.readline
N = int(input())
xy = [list(map(int, sys_input().split())) for _ in range(N)]
sorted_xy = sorted(xy, key=lambda x: (x[0], x[1]))

for xy in sorted_xy:
    print(xy[0], xy[1])
