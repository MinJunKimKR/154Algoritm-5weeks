import sys
input = sys.stdin.readline
n = int(input())
r = 10000000
arr = [True]*(r)
for i in range(2,int(r**0.5)+1):
    if arr[i]:
        for j in range(i*2,r,i):
            arr[j] = False
ans = []
while n != 1:
    for i in range(2,r):
        if arr[i] and n%i==0:
            ans.append(i)
            n//=i
            break
        else:
            continue
for i in ans:
    print(i)
