#2011
#실버1

n=list(map(int,input()))
l=len(n)
dp=[0 for x in range(l+1)]

if n[0] ==0:
    print("0")
    
else:
    n=[0]+n #두번째 조건을 위해서 0을 앞에 붙여줌.
    dp[0]=dp[1]=1
    
    for i in range(2,l+1):
        if n[i]>0:
            dp[i]+=dp[i-1]
            
        temp=n[i]+n[i-1]*10
        
        if temp<=26 and temp>=10:
            dp[i]+=dp[i-2]
    
    print(dp[l]% 1000000)
