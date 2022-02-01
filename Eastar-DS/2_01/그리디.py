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
