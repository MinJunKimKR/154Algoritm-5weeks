#2230
#골드5

#투포인터 사용..

n,m=map(int,input().split())
arr=[]

for i in range(n):
    arr.append(int(input()))
    
arr.sort() #정렬

start,end=0,1

mn=2000000000

while(start<n and end<n):
    if arr[end]-arr[start]<m:
        end+=1
    else:
        mn=min(mn,arr[end]-arr[start])
        start+=1
        
print(mn)
        


