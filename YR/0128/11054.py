#11054
#골드3
#가장 긴 바이토닉 부분 수열

n=int(input())

arr = list(map(int, input().split()))

dpup=[1 for x in range(n)]
dpdown=[1 for x in range(n)]
dpmx=[0 for x in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j]<arr[i]:
            dpup[i]=max(dpup[i],dpup[j]+1)

#arr.reverse()
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if arr[j]<arr[i]:
            dpdown[i]=max(dpdown[i],dpdown[j]+1)

#dpdown.reverse()
for i in range(n):
    dpmx[i]=dpup[i]+dpdown[i]
    

    
print(max(dpmx)-1)
            
