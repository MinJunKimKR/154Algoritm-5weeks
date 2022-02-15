#2003
#실버3

n,m=map(int,input().split())

arr=list(map(int,input().split()))

#투 포인터 이용
# 투포인터 : 두지점을 통해 구간의 부분합 도출
cnt=0
left,right=0,1

tmp=arr[left]

while left<=right and right<=n:
    
    sub_arr=arr[left:right]
    total_sum=sum(sub_arr)
    
    if total_sum==m:
        cnt+=1
        right+=1
    elif total_sum<m:
        right+=1
    elif total_sum>m:
        left+=1
print(cnt)
