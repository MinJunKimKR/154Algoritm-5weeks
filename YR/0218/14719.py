#14719
#골드5

#시뮬레이션
#스택이용하려고 했으나 어려워서 투포인터 이용해서 공부.

h,w=map(int,input().split())

arr=list(map(int,input().split()))

left=0
right=w-1

max_left=arr[left]
max_right=arr[right]

result=0

while left<right:
    max_left=max(max_left,arr[left])
    max_right=max(max_right,arr[right])
    
    if max_left<=max_right:
        result+=(max_left-arr[left])
        left+=1
    elif max_left>=max_right:
        result+=(max_right-arr[right])
        right-=1
        
print(result)
