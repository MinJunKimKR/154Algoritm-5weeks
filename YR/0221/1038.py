#골드5
#1038

#오후 1시 39분에 시작.
#브루트포스.
#n번째 감소하는 수가 어떻게 없지? -> 9876543210 이후에 감소하는 수는 업군아.

from collections import deque
n=int(input())

q=deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
total=9

if n<=9:
    print(n)
    exit()

while q:
    temp=q.popleft()
    for i in range(0,10):
        if str(i)>=temp[-1]:
            break
        q.append(temp+str(i))
        total+=1
        
        if total==n:
            print(q[-1])
            exit()
            
print(-1)
        
