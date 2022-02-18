n,k = map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))

cnt = 0
for i in reversed(arr):
    if k >= i:
        cnt += k // i
        k -= i*(k//i)

print(cnt)