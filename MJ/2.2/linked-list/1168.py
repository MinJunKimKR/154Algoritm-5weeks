# 12:15 -> 01:00

N, K = list(map(int, input().split()))

arr = [i for i in range(1, N+1)]

num = 0
print('<', end='')
while len(arr) > 1:
    num += K-1
    if num >= len(arr):
        num = num % len(arr)
    print(arr.pop(num), end=', ')
print(arr[0], end='')
print('>', end='')
