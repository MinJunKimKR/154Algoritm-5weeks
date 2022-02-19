#2096
#골드4
#슬라이딩 윈도우의 핵심 : 매번 처리되는 중복된 요소를 버리지 않고 재사용함으로서 낭비되는 계산을 하지 않음으로서 효율적으로 처리

#dp와 함께 사용하기도..

n=int(input())


maxarr=[[0 for x in range(3)] for y in range(2)]
minarr=[[0 for x in range(3)] for y in range(2)]

for i in range(n):
    a,b,c=(map(int,input().split()))
    
    maxarr[1][0]=max(maxarr[0][0],maxarr[0][1])+a
    minarr[1][0]=min(minarr[0][0],minarr[0][1])+a
    
    maxarr[1][1]=max(maxarr[0][0],maxarr[0][1],maxarr[0][2])+b
    minarr[1][1]=min(minarr[0][0],minarr[0][1],minarr[0][2])+b
    
    maxarr[1][2]=max(maxarr[0][2],maxarr[0][1])+c
    minarr[1][2]=min(minarr[0][2],minarr[0][1])+c
    
    maxarr[0][0],maxarr[0][1],maxarr[0][2]=maxarr[1][0],maxarr[1][1],maxarr[1][2]
    minarr[0][0],minarr[0][1],minarr[0][2]=minarr[1][0],minarr[1][1],minarr[1][2]

print(max(maxarr[0]),min(minarr[0]))
