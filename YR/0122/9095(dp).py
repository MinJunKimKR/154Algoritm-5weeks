#실버3
#bottom up을 사용할지 top down을 사용할지 자꾸 모르겠음.
#top down으로 접근 -> 재귀 사용
#초기값 설정.
#memoization하니까 런타임에러. 안하니까 해결됨
n=int(input())
dp=[0]*n

def sol(n):
    
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return sol(n-1)+sol(n-2)+sol(n-3)
        
for i in range(n):
    m=int(input())
    print(sol(m))


