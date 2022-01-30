# 2:24 -> 2:54
# 2:54 [FAIL-Memory overflow]

import sys
sys_input = sys.stdin.readline

N = int(input())
nums = [0]*10001
for _ in range(N):
    nums[int(sys_input())] += 1

num_str = ''
for idx in range(1, len(nums)):
    if N < 1:
        break
    if nums[idx] == 0:
        continue
    for _ in range(nums[idx]):
        N -= 1
        print(idx)
#         num_str += str(idx)+'\n'
# print(num_str, end='')
