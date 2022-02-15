#1806
#골드4

n,m=map(int,input().split())

arr=list(map(int,input().split()))

#투 포인터 이용
# 투포인터 : 두지점을 통해 구간의 부분합 도출

left,right=0,0

min=100001
total_sum=arr[0]

flag=0
while 1:
    
    if total_sum>=m:
        if min>right-left+1:
            min=right-left+1
        total_sum-=arr[left]
        left+=1
        flag=1
        
    elif total_sum<m:
        right+=1
        if right==n:
            break
        total_sum+=arr[right]
    
if flag==1:
    print(min)
else:
    print('0')
