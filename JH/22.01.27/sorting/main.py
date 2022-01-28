import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()
k -= 1
print(lst[k])