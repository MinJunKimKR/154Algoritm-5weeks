#1780
#분할정복
#실버2

#재귀?
mi=0
pl=0
ze=0

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

def sol(x,y,n):
    global mi,pl,ze
    num_chk=arr[x][y] #비교할 대상
    for i in range(x,x+n):
        #모두 같은 숫자로 써져있는지 확인
        for j in range(y,y+n):
            if arr[i][j] != num_chk:
                for k in range(3):
                    for l in range(3):
                        sol(x+k*n//3,x+l*n//3,n//3)
                return #return의 위치가 헷갈림 ㅜㅜ
    
    if num_chk==-1:
        mi+=1
    elif num_chk==0:
        ze+=1
    elif num_chk==1:
        pl+=1   

sol(0,0,n)
print(mi)
print(ze)
print(pl)
