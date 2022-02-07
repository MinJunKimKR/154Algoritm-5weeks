# 9:16 -> 9:46
# 9:58 [Success]
import math
from itertools import combinations


t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    total = 0
    combi_arr = list(combinations(arr, 2))
    for nums in combi_arr:
        total += math.gcd(nums[0], nums[1])
    print(total)
