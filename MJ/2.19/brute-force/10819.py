# 3:33 -> 4:03
# 3:56 [Success]
from itertools import permutations
N = int(input())
arr = list(map(int, input().split()))
permu_arr = list(permutations(arr, N))

max_result = 0


for random_arr in permu_arr:
    total = 0
    for i in range(N-1):
        total += abs(random_arr[i]-random_arr[i+1])
    max_result = max(max_result, total)

print(max_result)
