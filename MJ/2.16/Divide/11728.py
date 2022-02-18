# 9:20 -> 9:50
# 9:45 [success]
import sys
sys_input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, sys_input().strip().split()))
B = list(map(int, sys_input().strip().split()))


def devideMerge(arr):
    if len(arr) == 1:
        return arr
    mid_idx = len(arr)//2
    a_arr = devideMerge(arr[:mid_idx])
    b_arr = devideMerge(arr[mid_idx:])
    return sorted(a_arr + b_arr)


sorted_nums = devideMerge(A+B)

for i in sorted_nums:
    print(i, end=' ')
