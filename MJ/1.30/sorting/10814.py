# 1:58 -> 2:28
# 2:02[Success]
import sys
sys_input = sys.stdin.readline

N = int(input())
list = [[i]+sys_input().split() for i in range(N)]

sorted_list = sorted(list, key=lambda x: (int(x[1]), x[0]))
for list in sorted_list:
    print(list[1], list[2])
