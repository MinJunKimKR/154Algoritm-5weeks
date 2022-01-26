#스택
import sys
input = sys.stdin.readline
num = int(input())
arr=[]
for i in range(num):
    a = input().split()
    if a[0] == "push":
        arr.append(a[1])
    elif a[0] == "top":
        if arr:
            print(arr[-1])
        else:
            print(-1)
    elif a[0] == "size":
        print(len(arr))
    elif a[0] == "empty":
        if arr:
            print(0)
        else:
            print(1)
    elif a[0] == "pop":
        if not arr:
            print(-1)
        else:
            print(arr.pop())



