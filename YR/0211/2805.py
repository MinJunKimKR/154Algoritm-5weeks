#2805
#실버3
#분할정복-이분탐색

#높이의 범위가 1,000,000,000으로 제일 크군!

n,m=map(int,input().split())

arr=list(map(int,input().split()))

start,end=1,max(arr)

while(start<=end):
    tree_len=0
    mid=(start+end)//2 #나무의 길이
    
    for a in arr:
        if a>=mid: #조건 추가.
            tree_len+=(a-mid)
            if tree_len>m:
                break #추가해주면 시간초과가 안남.
    
    if tree_len>=m:
        start=mid+1
    else: 
        end=mid-1
        
print(end)
