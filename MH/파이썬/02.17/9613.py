from itertools import combinations
n = int(input())

def gcd(a,b):
    while a!=0:
        b %= a
        a,b = b,a
    return b

for _ in range(n):
    cnt=0
    arr = list(map(int,input().split()))
    arr=arr[1:]
    arr2 = list(combinations(arr,2))
    for a,b in arr2:
        cnt+=gcd(a,b)
    print(cnt)
