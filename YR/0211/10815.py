#10815
#실버5

#범위가 매우큼 -> 이분탐색 이용

#간단한 문제지만 이분탐색을 어떻게 이용해야 할지 모르겠군..
#요소들을 확인하는 문제는 이진탐색.
n=int(input())
arr=[]
check=[]

arr=list(map(int,input().split()))    
m=int(input())

check=list(map(int,input().split())) 

arr.sort()
    
def search(c,start,end):
    while(start<=end):
        mid=(start+end)//2
        
        if c>arr[mid]:
            start=mid+1
        elif c==arr[mid]:
            return 1
        else:
            end=mid-1
        
    return 0    
    
for c in check:
    if not search(c,0,n-1):
        print(0,end=' ')
    else:
        print(1,end=' ')
