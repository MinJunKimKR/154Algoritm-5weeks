#1043
#골드4



def find(a):
    if a==parent[a]:
        return a
    p=find(parent[a])
    parent[a]=p
    
    return parent[a]

def union(a,b):
    a=find(a)
    b=find(b)
    
    if a==b:
        return
    elif a<b:
        parent[b]=a
    else:
        parent[a]=b

def check(a,b):
    return find(a)==find(b)

n,m=map(int,input().split()) #사람수, 파티수

parent=[0]*(n+1)

for i in range(n+1):
    parent[i]=i #자기 자신을 부모로 초기화

know_truth=[0 for x in range(n+1)]
truth=list(map(int,input().split()))

t_num=truth[0]
truth=truth[1:]
for t in truth:
    know_truth[t]=1
    


#truth[0]에 진실아는 사람 수. 그 다음부터 진실아는사람 번호
arr=[]
for i in range(m):
    party=list(map(int,input().split()))
    
    p_num=party[0] #파티에 참석한 사람수
    party=party[1:] #파티에 참석한 인원 번호
    arr.append(party)
    #파티마다 입력되는사람들 그래프 묶고(union)진실을 아는 사람들과 같은 그래프에 있는지 확인(find)
    if p_num>1:
        for p in range(len(party)-1):
            union(party[p],party[p+1])

for i in range(1,n+1):
    if know_truth[i]==1:
        know_truth[find(i)]=1 #진실을 아는 사람들의 루트도 진실을 암.

if t_num==0:
    print(m)
else:
    cnt=0
    for p in arr:
        flag=1
        for j in p:
            if know_truth[find(j)]==1:
                flag=0 #진실을 아는사람이 있다면
            else:
                flag=1
        if flag==1:
            cnt+=1
    print(cnt)
            
    

