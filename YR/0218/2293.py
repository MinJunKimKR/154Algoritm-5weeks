#2293
#골드5

#슬라이딩 윈도우를 접목한 바텀업 방식으로 풀어야..

#다이나믹 프로그래밍 사용

n,m=map(int,input().split())
num=[]

for i in range(n):
    num.append(int(input()))
    
#coin(n,k)에서는 coin(n-1,k)단계의 답만 필요..
dp=[0 for x in range(k+1)]
dp[0]=1 #동전을 한개쓸때

for n in num:
    for j in range(i,k+1):
        if j-n>=0:
            dp[j]+=dp[j-n]

print(dp[k])
