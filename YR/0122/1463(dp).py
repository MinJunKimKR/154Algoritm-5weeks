#memoization 사용 -> memo배열 선언?
#해당 숫자랑 횟수 같이 저장? -> dic 사용?
#-> NO. 인덱스와 값이 숫자에 따른 횟수
#단순 구현이 아닌 이유: 반례가 존재하기 때문에
#점화식 세우기! dp(N) = min ( dp(N//3) +1, dp(N//2)+1 , dp(N-1)+1 )

n=int(input())
d=[0]*(n+1)

for i in range(2,n+1):

    d[i]=d[i-1]+1 #1을 뺐을 경우

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)	
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
print(d[n])
