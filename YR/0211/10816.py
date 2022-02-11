#10816
#실버4

#범위가 매우큼 -> 이분탐색 이용

#간단한 문제지만 이분탐색을 어떻게 이용해야 할지 모르겠군..
#요소들을 확인하는 문제는 이진탐색.
n=int(input())
arr=[]
check=[]

arr=list(map(int,input().split()))    
m=int(input())

check=list(map(int,input().split()))

count = {}
for a in arr:
    if a in count:
        count[a] += 1
    else:
        count[a] = 1 #각 숫자의 개수를 먼저 저장하고 시작..

arr.sort()
    
def search(c,start,end):
    count=0
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
    r=search(c,0,n-1)
    if r==1:
        print(count[c],end=' ')
    else:
        print(0,end=' ')
