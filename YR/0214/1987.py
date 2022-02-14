#1987
#골드4

r,c=map(int,input().split())

alpha=[]

for i in range(r):
    alpha.append(list(input()))

dx=[0,0,-1,1]
dy=[1,-1,0,0]

check=set() #check는 set으로 만들어서 메모리사용 줄이기 ㅜ
ans=0
def dfs(x,y,cnt):
    global ans
    ans=max(ans,cnt)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if 0<=nx<r and 0<=ny<c:
            if alpha[nx][ny] not in check:
                check.add(alpha[nx][ny])
                dfs(nx,ny,cnt+1)
                check.remove(alpha[nx][ny])
            


check.add(alpha[0][0])
dfs(0,0,1)
print(ans)
