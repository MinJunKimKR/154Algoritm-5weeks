#2110
#골드5
#분할정복-이분탐색

n,m=map(int,input().split())

#좌표의 범위 매우큼.
arr=[]

for i in range(n):
    arr.append(int(input()))

arr.sort()
start,end=1,(arr[-1]-arr[0])

while(start<=end):
    count=1 #공유기의 개수 초기화
    mid=(start+end)//2 #mid값이 두 공유기사이의 거리
    old=arr[0] #배열의 가장 낮은 좌표
    
    for i in range(1,len(arr)):
        if arr[i]>=old+mid:
            count+=1
            old=arr[i]
            if count>m:
                break
            
    if count>=m:
        start=mid+1
        answer=mid
    else:
        end=mid-1
print(answer)
        
    
    


        
    


    
    
