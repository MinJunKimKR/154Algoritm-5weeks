#1783
#실버4
#그리디

#이동횟수가 4번보다 작은 경우와 4번보다 큰 경우로 분리하여 문제를 해결해야함.
n,m=map(int,input().split())

count=0

#체스판은 최소 3x7 크기여야함.
if n==1:
    count=1
elif n==2: #세로 길이가 2라면, 4가지방향으로 이동불가능.
    count=(min((m+1)//2,4)) 
else:
    if m<7:#가로길이가 6이하라면, 4가지 방향으로 이동 불가능.
        count=(min(4,m))
    else:
        count=(m-2)
print(count)
    
