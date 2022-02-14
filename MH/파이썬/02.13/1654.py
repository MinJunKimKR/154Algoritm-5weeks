n,m = map(int,input().split())
line = []
for i in range(n):
    line.append(int(input()))
start = 1
end = max(line)
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in line:
        cnt += i//mid
    if cnt >= m:
        start = mid+1
    else:
        end = mid-1
print(end)


