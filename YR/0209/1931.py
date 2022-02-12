#1931
#실버2

#회의의 시작시간과 끝나는 시간이 같을수도 있다는 부분 check!
#->시작시간을 기준으로도 정렬해줘야 함.

n=int(input())
arr=[]
for i in range(n):
    start,end=map(int,input().split())
    arr.append([start,end])
    
arr=sorted(arr,key=lambda x:x[0])
arr=sorted(arr,key=lambda x:x[1])
count=1

start,end=arr[0][0],arr[0][1]
for i in range(1,len(arr)):
    a,b=arr[i][0],arr[i][1]
    if a>=end:
        start=a
        end=b
        count+=1

print(count)
