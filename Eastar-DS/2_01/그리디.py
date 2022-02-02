#그리디

#11047
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
prices,output = [],0
for _ in range(N):
    prices.append(int(input()))
N -= 1
while(K > 0):
    p = prices[N]
    if(K-p >= 0):
        output += (K//p)
        K %= p
    N-=1
print(output)


#2875
import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
maxteam = min(n//2, m)
n -= 2*maxteam
m -= maxteam
k -= (n+m)
if(k>0):
    maxteam -= k//3
    k %= 3
if(k>0):
    maxteam -= 1
print(maxteam)