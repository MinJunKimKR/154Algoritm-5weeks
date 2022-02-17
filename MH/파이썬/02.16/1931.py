n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
arr = sorted(arr,key = lambda x : (x[1],x[0]))

cnt=1
end_time = arr[0][1]
for i in range(1,n):
    if arr[i][0] >= end_time:
        cnt+=1
        end_time = arr[i][1]

print(cnt)