#2875
#브론즈3

n,m,k=map(int,input().split())

count=0

while (n>=2 and m>=1 and (n-2)+(m-1)>=k): #n,m의 범위가 작아서 while문 돌려도 될듯.
    n-=2 #여학생 2명뺌
    m-=1 #남학생 1명뺌
    count+=1
    
    
print(count)
