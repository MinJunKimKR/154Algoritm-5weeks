# 2805. 나무 자르기

import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(tree)

while start <= end:
    
    mid = (start + end) // 2
    
    length = sum(i - mid if i > mid else 0 for i in tree)
    
    '''
    for i in tree:
       if i >= mid:
           length += i - mid
    '''
    
    if length >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
