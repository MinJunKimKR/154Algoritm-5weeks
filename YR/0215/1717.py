#1717
#골드4

#서로소 집합, union find 사용.
#서로소 집합은 공통원소가 없는 두 집합.

n,m=map(int,input().split())
parent=[0 for i in range(n+1)]

for i in range(n+1):
    parent[i]=i #자기 자신을 부모로 설정
    
def find(a): #특정 원소가 속한 집합이 뭔지 알려주는 연산
    if a==parent[a]:
        return a #자기자신이 루트노드이면 자기자신 반환
    p=find(parent[a])#a의 루트노드 찾기
    parent[a]=p #부모테이블 갱신
    return parent[a] #a의 루트노드 반환

def union(a,b):#합집합 연산
    a=find(a)
    b=find(b) #a와 b의 루트노드 찾기
    
    if a==b:
        return #루트 노드가 같으면 동일한 집합
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
    
for i in range(m):
    check,a,b=map(int,input().split())
    if check==0:
        union(a,b)
        
    elif check==1:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
        
