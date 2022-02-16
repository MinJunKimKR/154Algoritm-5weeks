#1976
#골드4


#서로소 집합 사용하는 문제. 입력부분 어떻게 처리할지가 어려웠음
n=int(input())
cities=int(input())

        
parent=[0]*(n+1) 
for i in range(n+1):
    parent[i]=i #자기 자신으로 부모 초기화
    
def find(a):
    if a==parent[a]:
        return a
    p=find(parent[a]) #루트 노드 찾기
    parent[a]=p #부모 갱신
    
    return parent[a]

def union(a,b):
    a=find(a)
    b=find(b)
    
    if a==b:
        return #합칠필요가 없음(이미 동일한 집합)
    
    elif a<b:
        parent[b]=a
    else:
        parent[a]=b
        
for i in range(n):
    maps=list(map(int,input().split()))
    for x in range(len(maps)):
        if maps[x]==1: #연결되어있으면
            union(i+1,x+1)

plan=list(map(int,input().split()))
result=set()
for p in plan:
    result.add(find(p))

if len(result)==1:
    print('YES')
else:
    print('NO')
 
