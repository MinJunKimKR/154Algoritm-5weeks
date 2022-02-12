#1654
#실버3
#분할정복-이분탐색


k,n=map(int,input().split())
arr=[]

for i in range(k):
    arr.append(int(input()))

start,end=1,max(arr) #이분탐색 처음과 끝 위치

while start<=end:
    mid=(start+end)//2 #mid값에는 분할할 랜선의 길이가 담김
    lines=0 #랜선 수
    
    for i in arr:
        lines+=i//mid #lines에는 분할된 랜선 수가 담김.

    if lines>=n: #분할된 랜선 수가 요구사항보다 크면
        start=mid+1 #길이를 늘림
    else: #분할된 랜선 수가 요구사항보다 작으면
        end=mid-1 #길이를 줄임
print(end)
