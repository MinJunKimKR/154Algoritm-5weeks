n,m = map(int,input().split())
gap = []
for _ in range(n):
    gap.append(int(input()))
gap.sort()
start = 1
end = max(gap)-min(gap)

while start <= end:
    mid = (start+end)//2
    current = gap[0]
    count = 1

    for i in range(1,len(gap)):
        if gap[i] >= current + mid:
            count += 1
            current = gap[i]

    if count >= m:
        start = mid+1
    else:
        end = mid-1

print(end)