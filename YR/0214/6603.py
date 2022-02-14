#6603
#실버2

#permutation이 아닌 combination으로 해결 가능한 문제.


from itertools import combinations


while(1):
    arr=list(map(int,input().split()))
    
    if arr[0]==0:
        break
    
    result=list(combinations(arr[1:],6))
    
    for r in result:
        temp=list(r)
        print(*temp)
        
    print()
