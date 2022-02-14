#1759
#골드5

#bfs인듯.
from collections import deque

n,m=map(int,input().split())
alpha=list(map(str,input().split()))

alpha.sort()
answer=[]
def count(str): #모음개수 세는 함수
    cnt=0
    for i in range(len(str)):
        if str[i]=='a':
            cnt+=1
        elif str[i]=='e':
            cnt+=1
        elif str[i]=='i':
            cnt+=1
        elif str[i]=='o':
            cnt+=1
        elif str[i]=='u':
            cnt+=1
            
    return cnt

def count2(str): #모음개수 세는 함수
    cnt=0
    for i in range(len(str)):
        if str[i]=='a':
            continue
        elif str[i]=='e':
            continue
        elif str[i]=='i':
            continue
        elif str[i]=='o':
            continue
        elif str[i]=='u':
            continue
        else:
            cnt+=1
            
    return cnt

def bfs(v):
    queue=deque()
    queue.append(v)
    
    while(queue):
        temp=queue.popleft()
        
        if len(temp)==n and count(temp)>=1 and count2(temp)>=2:#조건을 만족할 때
            answer.append(temp)
            continue
        
        for a in alpha:
            if a>temp[-1]:
                queue.append(temp+a)
        
for a in alpha:
    bfs(a)
        
answer=(list(set(answer)))
answer.sort()
for a in answer:
    print(a)
