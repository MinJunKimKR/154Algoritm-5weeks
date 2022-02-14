n = int(input())
card = list(map(int,input().split()))
m = int(input())
card2 = list(map(int,input().split()))

card.sort()
ans = []
start = 0
end = n-1


def binary_search(start,end,target):
    while start <= end:
        mid = (start+end)//2
        if card[mid] < target:
            start = mid+1
        elif card[mid] == target:
            ans.append(1)
            return
        else:
            end = mid-1
    ans.append(0)

for i in card2:
    binary_search(0,n-1,i)

print(*ans)
