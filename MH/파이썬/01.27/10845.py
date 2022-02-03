#큐
import sys
input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
    a = list(input().split())
    if a[0] =='push':
        q.append(a[1])
    elif a[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)


